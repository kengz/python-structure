# python-structure
Sample project structure for a python package, contains all the necessary files to publish a PyPI package.


## Guide

- use `Python 3` and `pip3` like `npm`
- use `virtualenv` like `node_modules`

### Tool Installation

```bash
pip3 install virtualenvwrapper
echo "
# python virtualenv
source /usr/local/bin/virtualenvwrapper.sh" >> ~/.bash_profile
```

### Project creation

I'm assuming my PyPI package name is `structure`. Also, don't use non-alphabetic characters; for exampl PyPI will not allow '-' and '_'.

- create a project on Github, add `README, .gitignore, LICENSE`. Clone your git repo locally.
- update your `.gitignore` (see example) and remove `.md` from `README.md` cuz PyPI can't even
- create a `setup.py` (see example).
- make a folder with your package name to contain your source code. `mkdir structure` in my case.
- since the folder will be a module, add `structure/__init__.py`; this file will also contain the version, and the packaged methods.
- add any of your Python source code under `structure.py` and import the needed module methods in `structure/__init__.py`
- finally, at the root, do `pip3 freeze > requirements.txt` to generate list of dependencies you used, so it can install with `pip3 install -r requirements.txt`


### Packaging

Now that you have the project, it's time to publish. Navigate to the project root. First, register your package name; this may prompt you to create an account and login if it's your first time:

```
python setup.py register
```

Then, if the package name is registered successfully, upload your source to PyPI:

```
python setup.py sdist upload
```

Then wait for a **bazillion years** for PyPI to update it on their server before you can `pip install` it.


### Usage

The `./index.py` is a test file ignored in `setup.py`. A close thing to npm's `node_modules` is to create a virtual env to install dependencies and run code from:

```
# go to the root of your project folder to create env
virtualenv env
# activate the created virtual env
source env/bin/activate
# type 'deactivate' inside to quit

# install the package inside env
pip3 install -U structure
# Get ready the source code below before run:
python3 index.py
```


Inside `./index.py` there's a sample code:

```python
# the package
import structure

# using class
g1 = structure.greeter()
g1.greet()

# using module method
structure.hi()
```
