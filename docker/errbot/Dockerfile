FROM python:3.7-slim

ARG BUILD_DATE
ARG VCS_REF
LABEL maintainer="boidacarapreta@gmail.com" \
      org.label-schema.build-date=$BUILD_DATE \
      org.label-schema.name="ChatOps" \
      org.label-schema.description="Bot for apps deployment and maintanance" \
      org.label-schema.license="MIT" \
      org.label-schema.url="https://github.com/boidacarapreta/chat0ps" \
      org.label-schema.vcs-ref=$VCS_REF \
      org.label-schema.vcs-url="https://github.com/boidacarapreta/chat0ps" \
      org.label-schema.version="0.1.0" \
      org.label-schema.schema-version="1.0"\
      org.label-docker.cmd="/usr/local/bin/errbot"

COPY ./docker-entrypoint.sh /
COPY ./requirements.txt /
RUN chmod 0755 /docker-entrypoint.sh && \
    pip install -r /requirements.txt && \
    mkdir /errbot && \
    errbot --init /errbot && \
    apt update && \
    apt -y install git && \
    apt clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

VOLUME ["/errbot"]
WORKDIR "/errbot"
ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["/usr/local/bin/errbot"]
