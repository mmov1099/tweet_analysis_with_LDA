# setup
## copy repository
```bash
git clone https://github.com/mmov1099/tweet_analysis_with_LDA.git && \
cd tweet_analysis_with_LDA
```
## install MeCab
```bash
sudo apt-get install aptitude -y && sudo aptitude update && sudo aptitude upgrade -y && \
sudo aptitude install mecab libmecab-dev mecab-ipadic-utf8 git make curl xz-utils file -y && sudo cp /etc/mecabrc /usr/local/etc/
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


## search data
1．Get the top 50 trending

2．Save as json in `data/trend`

3．Search by the 50 trends obtained and retrieve the top 100 tweets in each of them

4．Save as json in `data/tweet`

```bash
python scripts/search_data.py
```

## periodically search data
search data every 3 hours
```bash
python scripts/schedule_do.py
```

# run
```bash
pwd
tweet_analysis_with_LDA
```
```python
python main.py
```
options
```python
python main.py -h
```
```bash
  -h, --help            show this help message and exit
  -nt NUM_TOPICS, --num_topics NUM_TOPICS
  -p, --preprocess      run preprocess
  -t, --train           run training LDA model
  -tf, --tfidf          use tfidf corpus
  -f, --feature         compress tweets and save features
  -e, --elbow           run elbow
  -nc NUM_CLUSTER, --num_cluster NUM_CLUSTER
  -k, --kmeans          run create_and_save_kmeans_model()
```
_______________________________________________________
under construction
# run scripts in a container
```bash
docker build -t lda .
docker run -it ubuntu /bin/bash
```

# for developping
```bash
cd ~/Documents_ubuntu/人工知能入門/final_report/scripts && source ../lda_env/bin/activate && python schedule_do.py
```
```bash
cd tweet_analysis_with_LDA/scripts && source ../lda_env/bin/activate && python schedule_do.py
```
