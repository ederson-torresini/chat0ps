# Kubernetes Access
The easier way to get Kubernetes cluster credentials is using `gcloud`. You may use [Cloud Shell](https://console.cloud.google.com/home/dashboard?cloudshell=true) and run:
```bash
gcloud container clusters get-credentials chatops --zone <insert you zone here> --project <insert you project here>
```
with [Terraform step 2 values](../terraform/) (zone or region in `zone`), which will create remote kubeconfig file.

If you prefer to use [kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl/) locally, you need to
copy and paste remote file `${HOME}/.kube/config` to local one with the same name. Then, go to [GKE Console](https://console.cloud.google.com/kubernetes/list), choose the cluster and `show credentials` button. You'll see username, password and certificate data. In kubeconfig file, update only inside `users` scope, specially `username` and `password`, like this:
```yaml
apiVersion: v1
clusters:
- cluster:
    certificate-authority-data: <certificate in Base64 format>
    server: <API URL>
  name: <cluster name>
contexts:
- context:
    cluster: <cluster name>
    user: <cluster username>
  name: <cluster context name>
current-context: <cluster context name>
kind: Config
preferences: {}
users:
- name: <cluster username>
  user:
    username: <username>
    password: <password>
```

# Errbot + Telegram
Errbot has many backends. This example uses Telegram as mentioned in [my errbot Docker image](../docker/errbot/).

Follow these steps to run a chatbot using Telegram.
1. First, you need to [create a Telegram bot](https://telegram.me/BotFather). The process you return you the bot token, which will be needed soon.

2. Errbot uses a main configuration file, `config.py`. Create this file like this example. Please, don't forget to change `token` (from step 1) and `BOT_ADMINS` (your Telegram number).
```python
# Logging to stdout
import logging
BOT_LOG_FILE = None
BOT_LOG_LEVEL = logging.INFO

# Persistent data
BOT_DATA_DIR = r'/errbot/data'
BOT_EXTRA_PLUGIN_DIR = r'/errbot/data/plugins'

#Backend configuration
BACKEND = 'Telegram'
BOT_IDENTITY = {'token': '<insert your token here>',}
BOT_ADMINS = ('<insert you nickname here later>',)

# How to call bot in chat
BOT_PREFIX_OPTIONAL_ON_CHAT = True
BOT_PREFIX = '/'
CHATROOM_PRESENCE = ()

# Auto install plugin dependencies
AUTOINSTALL_DEPS = True
```
You can give many users as bot admins - just separate with commas. For the first time, the list must be empty (`BOT_ADMINS = ()`). Later, the command `whoami` is really useful to tell your Telegram number.

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
