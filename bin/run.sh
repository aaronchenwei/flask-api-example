#!/usr/bin/env bash

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"

gunicorn -c $SCRIPT_DIR/gunicorn.py --chdir ../ wsgi:app
