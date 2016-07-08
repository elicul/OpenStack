# -*- coding: utf-8 -*-

import argparse
import subprocess

parser = argparse.ArgumentParser()
parser.add_argument("name", help="Instance name")
args = parser.parse_args()

instance_name = args.name

if instance_name == 'instance_0':
  #Instalacija Chef Servera
  subprocess.call("~/OpenStack/chef_server.sh", shell=True)
  #admin
  #mypassword
  
elif instance_name == 'instance_1':
  #Instalacija Chef Workstationa
  subprocess.call("~/OpenStack/chef_workstation.sh", shell=True)
else:
  #Instalacija Chef Clienta
