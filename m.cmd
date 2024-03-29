@ECHO OFF

IF EXIST %VIRTUAL_ENV% GOTO do_m

:load_venv
    ECHO Loading venv
    CALL .\python\Scripts\activate.bat
    GOTO do_m

:do_m

python setup.py sdist bdist_wheel

pip install --upgrade .\dist\rss2diaspora_spider_Spidey01-0.0.1-py3-none-any.whl

python .\python\Scripts\rss2diaspora-spider %*
