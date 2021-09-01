#!/bin/bash

export PYTHON_APP_HOME=`pwd`

cd src
mypy app.py
mypy util.py
# python app.py
