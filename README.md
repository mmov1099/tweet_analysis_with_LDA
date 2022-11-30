# setup
## MeCab
```bash
sudo apt-get install aptitude -y && sudo aptitude update && sudo aptitude upgrade -y
sudo aptitude install mecab libmecab-dev mecab-ipadic-utf8 git make curl xz-utils file -y
git clone --depth 1 https://github.com/neologd/mecab-ipadic-neologd.git
cd mecab-ipadic-neologd
./bin/install-mecab-ipadic-neologd -n -y
cd .. && rm -rf mecab-ipadic-neologd
sudo aptitude install swig -y
sudo aptitude install python3-pip -y
python3 -m venv lda_env
source lda_env/bin/activate
pip install -r requirements.txt
```


## When you run scripts
```bash
cd scripts
```

# search data
1．トレンド上位50個を取得

2．`data/trend`にjsonで保存

3．取得したトレンド50個で検索してそれぞれで上位100個のツイートを取得

4．`data/tweet`にjsonで保存

```bash
python search_data.py
```

# 定期的にsearch data
3時間おきにsearch data
```bash
python schedule.py
```

# 作業用
```bash
cd ~/Documents_ubuntu/人工知能入門/final_report/scripts && source ../lda_env/bin/activate && python schedule_do.py
```