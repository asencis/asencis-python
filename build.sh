#!/bin/sh
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
python setup.py sdist bdist_wheel
twine check dist/*
twine upload dist/*
