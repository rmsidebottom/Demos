#!/bin/bash

sudo pip install virtualenv
virtualenv SessionMgmt
SessionMgmt/bin/pip install -r requirements.txt

SessionMgmt/bin/python app.py
