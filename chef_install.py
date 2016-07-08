# -*- coding: utf-8 -*-

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("name", help="Instance name")
args = parser.parse_args()

instance_name = args.name

if instance_name == 'instance_0':
  #Instalacija Chef Servera
  bash = "sudo apt-get update"
  os.system(bash)
  bash = "wget https://opscode-omnibus-packages.s3.amazonaws.com/ubuntu/12.04/x86_64/chef-server_11.1.3-1_amd64.deb"
  os.system(bash)
  bash = "sudo dpkg -i chef-server*"
  os.system(bash)
  bash = "rm chef-server-core_*.deb"
  os.system(bash)
  bash = "sudo chef-server-ctl reconfigure"
  os.system(bash)
  bash = "sudo chef-server-ctl test"
  os.system(bash)
  #open port 443 in the security group associated with the server
  #https://{your_server_domain_or_IP}
  #default login credentials
  #admin
  #p@ssw0rd1
  
elif instance_name == 'instance_1':
  #Instalacija Chef Workstationa
  bash = "sudo apt-get update"
  os.system(bash)
  bash = "sudo apt-get install git"
  os.system(bash)
  bash = "curl -L https://www.opscode.com/chef/install.sh | sudo bash"
  os.system(bash)
  bash = "cd ~"
  os.system(bash)
  bash = "git clone https://github.com/opscode/chef-repo.git"
  os.system(bash)
  bash = "mkdir ~/chef-repo/.chef"
  os.system(bash)
else:
  #Instalacija Chef Clienta
