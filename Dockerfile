FROM jenkins/jenkins:lts
USER root
RUN apt-get update \
    && apt-get install -y python3-pip python3.5 \
    && rm -rf /var/lib/apt/lists/*
RUN pip3 install tox
