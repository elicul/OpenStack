# -*- coding: utf-8 -*-

import argparse
import subprocess

parser = argparse.ArgumentParser()
parser.add_argument("name", help="Instance name")
parser.add_argument("ip", help="Instance public ip")
args = parser.parse_args()

instance_name = args.name
ip = args.ip

if instance_name == 'instance_0':
	#Instalacija Chef Servera
  	subprocess.call("~/OpenStack/chef_server.sh", shell=True)

	# Open a file
	fo = open("knife.rb", "wb")
	fo.write( """
					current_dir = File.dirname(__FILE__)
					log_level                :info
					log_location             STDOUT
					node_name                "admin"
					client_key               "#{current_dir}/admin.pem"
					validation_client_name   "upi-validator"
					validation_key           "#{current_dir}/upi.pem"
					chef_server_url          "https://""" + ip + """/organizations/upi"
					cache_type               'BasicFile'
					cache_options( :path => "#{ENV['HOME']}/.chef/checksums" )
					cookbook_path            ["#{current_dir}/../cookbooks"]

					### Knife-OpenStack Access Credentials
					knife[:openstack_username] = "Students"
					knife[:openstack_password] = "PW3jMT"
					knife[:openstack_tenant] = "Student"
					knife[:openstack_auth_url] ="https://upi_auth_ip:8770/v2.0/tokens"
		""");

	# Close opend file
	fo.close()
  	#admin
  	#mypassword
  
elif instance_name == 'instance_1':
  	#Instalacija Chef Workstationa
  	subprocess.call("~/OpenStack/chef_workstation.sh", shell=True)
else:
  	#Instalacija Chef Clienta
	subprocess.call("~/OpenStack/chef_client.sh " + instance_name, shell=True)