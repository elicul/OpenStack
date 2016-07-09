#!/bin/bash

wget https://opscode-omnibus-packages.s3.amazonaws.com/ubuntu/12.04/x86_64/chefdk_0.5.1-1_amd64.deb
sudo dpkg -i chefdk_*.deb
rm chefdk_*.deb
chef verify

git clone git://github.com/chef/chef-repo.git
echo ".chef" >> ~/chef-repo/.gitignore

scp opc@10.20.0.1:~/admin.pem ~/chef-repo/.chef
scp opc@10.20.0.1:~/upi.pem ~/chef-repo/.chef

cp ~/OpenStack/knife.rb ~/chef-repo/.chef/knife.rb
sudo /opt/chef/embedded/bin/gem install knife-openstack

knife ssl fetch
knife client list