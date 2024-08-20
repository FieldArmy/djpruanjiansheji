#!/bin/bash
DIR="$( cd "$( dirname "$0" )" && pwd )"
echo $DIR

cd $DIR

# ulimit -n 50000
nohup gunicorn --config=gk_back/gunicorn_conf.py gk_back.wsgi &> /dev/null &