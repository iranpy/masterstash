Masterstash: Lightweight Log Collector
============================


Installation
----------------------------------
Ums runs on python 3.

#### Setup Python environment
    $ Install PIP On Debian/Ubuntu sudo apt-get install python3-pip python3-dev
    $ Install PIP On Arch sudo pacman -S python-pip
    $ sudo pip3 install virtualenvwrapper

#### Setup virtual environment

    $ echo "export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3" >> ~/.bashrc
    $ echo "alias env.activate=\"source /usr/bin/virtualenvwrapper.sh\"" >> ~/.bashrc & source ~/.bashrc
    $ env.activate
    $ mkvirtualenv --python=$(which python3) --no-site-packages masterstash

#### Installing

    $ cd path/to/ums/src
    $ pip install -e .
