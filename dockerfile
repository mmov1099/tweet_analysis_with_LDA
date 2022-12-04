FROM ubuntu
RUN apt update && apt upgrade -y

#install MeCab
RUN apt-get install -y sudo \
    && sudo apt-get install aptitude -y \
    && sudo aptitude update && sudo aptitude upgrade -y \
    && sudo aptitude install -y \
    mecab \
    libmecab-dev \
    mecab-ipadic-utf8 \
    make \
    curl \
    xz-utils \
    git \
    file
#install NEologd
RUN git clone --depth 1 https://github.com/neologd/mecab-ipadic-neologd.git \
    && cd mecab-ipadic-neologd \
    && ./bin/install-mecab-ipadic-neologd -n -y \
    && cd .. && rm -rf mecab-ipadic-neologd
#install python and make virtual env, install packages
RUN apt-get install -y \
    swig \
    python3 \
    python3-pip

COPY requirements.txt /tmp/
RUN pip install -r /tmp/requirements.txt
COPY . /tmp/

WORKDIR /tmp/