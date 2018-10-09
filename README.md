# Chat0ps
How to teach DevOps?
This is an effort to show a path to learn: concepts like virtualization, tools and so forth.

# Virtualization
Compute, storage and network.

## Infrastructure-as-Code
[Terraform](https://terraform.io) to create an environment to run applications.

## Kubernetes
Used [Google Kubernetes Engine](https://cloud.google.com/kubernetes-engine/), but no Google-only tool has been used (as I can remember).

## Containers

### Mongo
The [official MongoDB](https://hub.docker.com/_/mongo/) container has been used.

### Errbot
My Errbot solution uses Slack backend, so I made my own container ([source](/docker/errbot/) and [image](https://hub.docker.com/r/boidacarapreta/errbot/)).

[![](https://images.microbadger.com/badges/image/boidacarapreta/errbot.svg)](https://microbadger.com/images/boidacarapreta/errbot "Get your own image badge on microbadger.com")
[![](https://images.microbadger.com/badges/commit/boidacarapreta/errbot.svg)](https://microbadger.com/images/boidacarapreta/errbot "Get your own commit badge on microbadger.com")
[![](https://images.microbadger.com/badges/license/boidacarapreta/errbot.svg)](https://microbadger.com/images/boidacarapreta/errbot "Get your own license badge on microbadger.com")

# Programming
Most universities teach Python as the first language programming.
To my experience, that's a good approach: smooth learning curve, well documented data structures, a lot of libraries and, of course, an easy-to-use chatbot to [develop plugins](/srv/errbot/plugins/).
