#!/bin/bash
ssh -i UPI.key ubuntu@10.20.0.2
cd ~/chef-repo
knife bootstrap -x ubuntu -i ~/OpenStack/UPI.key $1 --sudo