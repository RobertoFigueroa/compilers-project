#!/bin/sh
export FLASK_APP=./server.py
source $(venv) venv/bin/activate
flask run