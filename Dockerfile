FROM python:3.6
MAINTAINER aerospaceresearch Team

EXPOSE 8023

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && apt-get install -y \
    bash \
    curl \
    g++ \
    git \
    lib32z1-dev \
    libfreetype6-dev \
    libjpeg-dev \
    libmemcached-dev \
    libxml2-dev \
    libxslt1-dev \
    locales \
    postgresql-client \
    postgresql-server-dev-all \
    sudo \
    zlib1g-dev \
    && rm -rf /var/lib/apt/lists/*

ADD requirements.txt /opt/code/requirements.txt
WORKDIR /opt/code
RUN pip3 install -Ur requirements.txt
ADD . /opt/code

# user
RUN useradd uid1000 -d /home/uid1000
RUN mkdir -p /home/uid1000 && chown uid1000: /home/uid1000
VOLUME /home/uid1000

RUN chown -R uid1000: /opt

USER uid1000

WORKDIR /opt/code/gsapi/

# production stuff
ENTRYPOINT ["./start.sh"]
CMD ["web"]
