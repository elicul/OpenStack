#!/bin/bash

wget https://opscode-omnibus-packages.s3.amazonaws.com/ubuntu/12.04/x86_64/chef-server_11.1.3-1_amd64.deb
sudo dpkg -i chef-server*
rm chef-server-core_*.deb
sudo chef-server-ctl reconfigure

sudo chef-server-ctl user-create admin admin admin elicul@riteh.hr mypassword -f ~/admin.pem
sudo chef-server-ctl org-create upi upi_cloud --association_user admin --filename ~/upi.pem
