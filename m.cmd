@ECHO OFF

python setup.py sdist bdist_wheel

pip install --upgrade .\dist\RSS2Diaspora_Spider*-py3-none-any.whl

python .\python\Scripts\rss2diaspora-spider %*
