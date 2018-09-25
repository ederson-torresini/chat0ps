import json
from errbot import BotPlugin, botcmd, webhook

class Webhook(BotPlugin):
    """Webhook for GitOps"""

    @webhook(raw=True)
    def publish(self, request):
        """Webhook URL for git publishes"""
        if request.get_header('user-agent').split('/')[0] == 'GitHub-Hookshot':
            payload = request.json
            self.warn_admins('GitHub notification:'
                             + ' user ' + payload['pusher']['email']
                             + ' just pushed in ' + payload['repository']['name']
                             + '. You may look the diff: ' + payload['compare'] + '.')

        #self.send(
        #    self.build_identifier('@boidacarapreta'),
        #    'Oi'
        #    # 'Commit on %s!' % payload['repository']['name'],
        #)

    #@botcmd(split_args_with=None)
    #def subscribe(self, msg, args):
    #    yield msg
    #    yield args
        
