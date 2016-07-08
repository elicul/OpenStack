#!/bin/bash

sudo apt-get update
sudo apt-get install git python

git clone https://github.com/elicul/OpenStack.git

python OpenStack/chef_install.py
