from errbot import BotPlugin, botcmd, webhook
from bottle import abort
from requests import head, codes


class GitOps(BotPlugin):
    """Gitops integration: PubSub via Webhook"""

    @webhook(raw=True)
    def publish(self, request):
        """Webhook for git pushes"""
        if request.get_header('user-agent').split('/')[0] == 'GitHub-Hookshot':
            payload = request.json
            self.warn_admins('GitHub notification: new commit(s) in ' + payload['repository']['name']
                             + ' pushed by user ' + payload['pusher']['email']
                             + '. You can look the diff in ' + payload['compare'] + '.')
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
            yield 'Please inform repository URL.'
            return

        elif len(args) >= 2:
            yield 'Taking only the first argument as URL (discarding the rest...).'
        url = args[0]
        yield 'Trying to reach site. Please wait a moment...'
        try:
            response = head(url)
        except:
            yield 'Invalid URL. Please inform a valid one.'
            return

        if response.status_code == codes.ok:
           yield 'Success! Subscribing "' + msg.frm.person + '" to "' + url + '"...'
        else:
            yield 'Failure! HTTP response: ' + str(response.status_code) + '.'
 

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
        yield msg
