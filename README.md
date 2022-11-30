# setup
## copy repository
```bash
git clone https://github.com/mmov1099/tweet_analysis_with_LDA.git && \
cd tweet_analysis_with_LDA
```
## install MeCab
```bash
sudo apt-get install aptitude -y && sudo aptitude update && sudo aptitude upgrade -y && \
sudo aptitude install mecab libmecab-dev mecab-ipadic-utf8 git make curl xz-utils file -y
```
## install NEologd
```bash
git clone --depth 1 https://github.com/neologd/mecab-ipadic-neologd.git && \
cd mecab-ipadic-neologd && ./bin/install-mecab-ipadic-neologd -n -y && \
cd .. && rm -rf mecab-ipadic-neologd
```
## install python and make virtual env , install packages
```bash
sudo aptitude install swig -y && sudo aptitude install python3-pip -y \
python3 -m venv lda_env && source lda_env/bin/activate && \
pip install -r requirements.txt
```

## when you run scripts
```bash
cd scripts
```

# search data
1．Get the top 50 trending

2．Save as json in `data/trend`

3．Search by the 50 trends obtained and retrieve the top 100 tweets in each of them

4．Save as json in `data/tweet`

```bash
python search_data.py
```

# periodically search data
search data every 3 hours
```bash
python schedule.py
```

# for developping
```bash
cd ~/Documents_ubuntu/人工知能入門/final_report/scripts && source ../lda_env/bin/activate && python schedule_do.py
```
```bash
cd tweet_analysis_with_LDA/scripts && source ../lda_env/bin/activate && python schedule_do.py
```