# README

RSSフィードを読み込んで内容を出力するスクリプトです。  
python2.7で動作します。

某社のスキルチェックの課題で作成してBitBucketのプライベートレポジトリに入れていたのをこちらに引っ越しました。  

## Download
```
# git clone git@bitbucket.org:hfujima/rssreader.git
```

## Setup
### 0) pipのインストール
Pythonのパッケージ管理システムのpipがローカルに入っていない場合はインストールしてください。
```
# curl https://bootstrap.pypa.io/get-pip.py > ./get-pip.py
# sudo python ./get-pip.py
```
see: https://pip.pypa.io/en/stable/installing/

### 1) virtualenvの設定
必須ではないですがローカル環境のpythonを汚したくない場合はvirtualenvを使用してください。
```
# pip install virtualenv
# cd {rssreader}
# virtualenv --clear ./virtualenv
# source ./virtualenv/bin/activate
```

### 2) 必須ライブラリのインストール
beautifulsoup4とpytzを使用しているのでローカル環境にインストールしてください。
```
# pip install -r {rssreader}/requirements.txt
```

## 実行方法
URLを指定して実行する
```
# {rssreader}/read_rss.sh http://news.yahoo.co.jp/pickup/rss.xml
```

ローカルに配置されたRSSファイルを指定して実行する
```
# {rssreader}/read_rss.sh --file {rssreader}/yahoo.xml
```

タイトルだけを出力する
```
# {rssreader}/read_rss.sh --format "title:{title}" http://news.yahoo.co.jp/pickup/rss.xml
```
