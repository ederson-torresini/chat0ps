# Chat0ps
How to teach DevOps?
This is an effort to show a path to learn: concepts like virtualization, tools and so forth.

# Virtualization
Compute, storage and network.

## Containers

### Mongo
The [official MongoDB](https://hub.docker.com/_/mongo/) container has been used.

### Errbot
My Errbot solution uses Telegram backend, so I made my own container.

[![](https://images.microbadger.com/badges/image/boidacarapreta/errbot.svg)](https://microbadger.com/images/boidacarapreta/errbot "Get your own image badge on microbadger.com")
[![](https://images.microbadger.com/badges/commit/boidacarapreta/errbot.svg)](https://microbadger.com/images/boidacarapreta/errbot "Get your own commit badge on microbadger.com")
[![](https://images.microbadger.com/badges/license/boidacarapreta/errbot.svg)](https://microbadger.com/images/boidacarapreta/errbot "Get your own license badge on microbadger.com")

**[Check the code](/docker/errbot/)**.

## Infrastructure-as-Code
[Terraform](https://terraform.io) was used to create an environment to run applications. More specifically, an environment on [Google Kubernetes Engine](https://cloud.google.com/kubernetes-engine/) ([Google Cloud Platform](https://cloud.google.com)).

**[Check the code](/terraform/)**.

## Kubernetes
With the containers images and a running Kubernetes cluster, you can deploy the services: backend database and frontend chatbot.

**[Check the code](/kubernetes/)**.

# Programming
Most universities teach Python as the first language programming.
To my experience, that's a good approach: smooth learning curve, well documented data structures, a lot of libraries and, of course, an easy-to-use chatbot to develop plugins.

**[Check the code](/srv/errbot/plugins/)**.
