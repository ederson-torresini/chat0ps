# Errbot + Slack
Errbot has many backends. This example uses Slack as mentioned in [my errbot Docker image](../docker/errbot/).

Follow these steps to run a chatbot using Slack.
1. First, you need to [create a Slack bot](https://api.slack.com/apps). The process you return you the bot token, which will be needed soon.

2. Errbot uses a main configuration file, `config.py`. Create this file like this example. Please, don't forget to change `token` (from step 1) and `BOT_ADMINS` (your Slack nickname with preceding "`@`").
```python
# Logging to stdout
import logging
BOT_LOG_FILE = None
BOT_LOG_LEVEL = logging.INFO

# Persistent data
BOT_DATA_DIR = r'/errbot/data'
BOT_EXTRA_PLUGIN_DIR = r'/errbot/data/plugins'

#Backend configuration
BACKEND = 'Slack'
BOT_IDENTITY = {
    'token': '<insert your token here>',
}
BOT_ADMINS = ('<insert you nickname here>',)

# How to call bot in chat
BOT_PREFIX_OPTIONAL_ON_CHAT = True
BOT_PREFIX = '!'

# Auto install plugin dependencies
AUTOINSTALL_DEPS = True
```
You can give many users as bot admins - just separate with commas.

3. Convert `config.py` into Base64 format (command `base64`) with no newline (`tr -d '\n'`):
```bash
cat config.py | base64 | tr -d '\n'
```
and append the result to `config.py`:
```yaml
apiVersion: v1
kind: Secret
metadata:
  name: errbot
  labels:
    app: chatops
    tier: frontend
type: Opaque
data:
  config.py: <config.py content file in base64 format>
```
Name this new file as `Secret.yaml`

4. With the Secret file, create the object into the cluster:
```bash
kubectl create -f Secret.yaml
```

5. At last, populate with all the remaining objects:
```bash
kubectl create -f gcp.yaml
```

6. You may see all objects with:
```bash
kubectl get secrets,pvc,svc,deployments
```
But, honestly, I suggest you to use the [GKE console](https://console.cloud.google.com/kubernetes/list), the [Kubernetes default dashboard](https://github.com/kubernetes/dashboard) or even a third-party application/service. [Weave Cloud](https://cloud.weave.works) is a nice one!
