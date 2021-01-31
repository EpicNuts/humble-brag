FROM python:3.7.5-slim-buster
MAINTAINER ben

ENV INSTALL_PATH /humbleBrag
RUN mkdir -p $INSTALL_PATH

WORKDIR $INSTALL_PATH

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD gunicorn -b 0.0.0.0:8000 --access-logfile - "humbleBrag.app:create_app()"
