FROM ubuntu:focal

ENV DEBIAN_FRONTEND=noninteractive
RUN apt update && \
    apt install -y npm sqlite3 python-is-python3 python3-pip && \
    rm -rf /var/lib/apt/lists/*

RUN npm install -g bower && \
    npm install -g gulp-cli && \
    pip3 install pipenv

