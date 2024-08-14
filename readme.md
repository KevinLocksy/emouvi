# Emouvi

Python project to create mouving emoji from a sequence of emojis

## Virtual environment

- pip install virtualenv
- create a virtual env: python -m venv __myenv__
- activate the virtual env __myenv__\Scripts\activate

## Installation

#### setup.py
- create a package module : `folder/subfolder/__init__.py`
- define it in setup.py in '`setup{    packages=["module.emouvi"],}`
- if pip is not installed, install pip by running `python -m pip install --upgrade pip`
- install the module with pip : `pip install -e .` -e = editable (for dev, otherwise usual install `pip install .`)
- run your script: `python .\scripts\index.py`
if you want to run a test module, modify the setup file..