#!/bin/sh

if [ -z "$VIRTUAL_ENV" ]; then
    echo "Loading venv"
    . ./python/bin/activate
fi

python setup.py sdist bdist_wheel

pip install --upgrade ./dist/rss2diaspora_spider_Spidey01-0.0.1-py3-none-any.whl

python ./python/Scripts/rss2diaspora-spider $*
