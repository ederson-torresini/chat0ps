from errbot import BotPlugin, botcmd, webhook, ONLINE, AWAY
from bottle import abort
from requests import head, codes
from pymongo import MongoClient

class GitOps(BotPlugin):
    """Gitops integration: PubSub via Webhook"""


    def check_mongo(self):
        client = MongoClient()
        try:
            response = client.chat0ps.command("ping")
        except:
            self.change_presence(AWAY)
            self.warn_admins("MongoDB down!")
            self.stop_poller(self.check_mongo)
        else:
            self.change_presence(ONLINE)


    def activate(self):
        super().activate()
        self.start_poller(10, self.check_mongo)


    @botcmd(split_args_with=None)
    def mongodb_up(self, msg, args):
        """
        Notify chatbot MongoDB is up and running.
        """
        if (self.check_mongo, [], {}) in self.current_pollers:
            yield "Command ignored: bot already notified."
        else:
            yield "Restarting poller: MongoDB status check..."
            self.start_poller(10, self.check_mongo)
            yield "Done."


    @webhook(raw=True)
    def publish(self, request):
        """Webhook for git pushes"""
        if request.get_header("user-agent").split("/")[0] == "GitHub-Hookshot":
            payload = request.json
            self.warn_admins("GitHub notification: new commit(s) in "
                             + payload["repository"]["name"]
                             + " pushed by user " + payload["pusher"]["email"]
                             + ". You can look the diff in " + payload["compare"] + ".")
        else:
            # For now, just GitHub webhooks are accepted.
            # Soon others providers, like GitLab, will be available.
            abort(400, "Bad Request")

    @botcmd(split_args_with=None)
    def subscribe(self, msg, args):
        """
        Subscribe to repository notifications.
        It takes only one mandatory argument: the respository URL (must be public HTTP or HTTPS).
        """
        if len(args) == 0:
            yield "Please inform repository URL."
            returnd
        elif len(args) >= 2:
            yield "Taking only the first argument as URL (discarding the rest...)."
        url = args[0]
        yield "Trying to reach site. Please wait a moment..."
        try:
            response = head(url)
        except:
            yield "Invalid URL. Please inform a valid one."
            return
        if response.status_code == codes.ok:
            yield "Success! Subscribing to " + url + "..."
            document = {
            "repository": url,
                "subscribers": [
                    msg.frm.person
                ]
            }
            client = MongoClient()
            if client.chat0ps.subscriptions.find(document):
                yield "Repository already subscribed."
            else:
                client.chat0ps.subscriptions.insert_one(document)
                yield "Done."
        else:
            yield "Failure! HTTP response: " + str(response.status_code) + "."


    @botcmd(split_args_with=None)
    def unsunscribe(self, msg, args):
        """
        Unsubscribe to repository notifications
        It takes only one mandatory argument: the repository URL.
        """
        for arg in args:
            yield arg


    @botcmd
    def subscriptions(self, msg, args):
        """
        List all repository subscriptions.
        """
        client = MongoClient()
        query = {
            "subscribers": msg.frm.person
        }
        for subscription in client.chat0ps.subscriptions.find(query):
            yield subscription['repository']
