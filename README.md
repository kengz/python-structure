# python-structure
Sample project structure for a python package.

## Guide

- use `Python 3` and `pip3` like `npm`
- use `virtualenv` like `node_modules`

#### Installation

```bash
pip3 install virtualenvwrapper
echo "
# python virtualenv
source /usr/local/bin/virtualenvwrapper.sh" >> ~/.bash_profile

# activate the created virtual env
virtualenv env
source env/bin/activate
# generate dep list for use in pip3 install -r requirements.txt
pip3 freeze > requirements.txt
# the type 'deactivate' inside to quit
```