#!/bin/bash

export PYTHON_APP_HOME=`pwd`

cd src
mypy app.py
# python app.py
