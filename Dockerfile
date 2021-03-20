FROM python:3

# 環境変数(PYTHONUNBUFFEREDに1を設定)
ENV PYTHONUNBUFFERED 1

#  codeディレクトリを作成
RUN mkdir /code

# 作業用のディレクトリに移動			
WORKDIR /code

# requirements.txtから必要なライブラリをインストール	
ADD requirements.txt /code/
RUN pip install -r requirements.txt

# ローカルのコード（ファイル）をcodeにコピー
ADD . /code/