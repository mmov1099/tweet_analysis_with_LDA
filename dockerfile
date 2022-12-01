FROM ubuntu:20.04
RUN apt update && apt upgrade

#copy repository
RUN sudo apt-get install git -y
RUN git clone https://github.com/mmov1099/tweet_analysis_with_LDA.git && \
cd tweet_analysis_with_LDA
#install MeCab
RUN sudo apt-get install aptitude -y && sudo aptitude update && sudo aptitude upgrade -y && \
sudo aptitude install mecab libmecab-dev mecab-ipadic-utf8 git make curl xz-utils file -y
#install NEologd
RUN git clone --depth 1 https://github.com/neologd/mecab-ipadic-neologd.git && \
cd mecab-ipadic-neologd && ./bin/install-mecab-ipadic-neologd -n -y && \
cd .. && rm -rf mecab-ipadic-neologd
#install python and make virtual env, install packages
RUN sudo aptitude install swig -y && sudo aptitude install python3-pip -y \
python3 -m venv lda_env && source lda_env/bin/activate

COPY requirements.txt /tmp/
RUN pip install /tmp/requirements.txt
COPY . /tmp/