current_dir = File.dirname(__FILE__)
log_level                :info
log_location             STDOUT
node_name                "admin"
client_key               "#{current_dir}/admin.pem"
validation_client_name   "upi-validator"
validation_key           "#{current_dir}/upi.pem"
chef_server_url          "https://<chef server name or IP>/organizations/upi"
cache_type               'BasicFile'
cache_options( :path => "#{ENV['HOME']}/.chef/checksums" )
cookbook_path            ["#{current_dir}/../cookbooks"]

### Knife-OpenStack Access Credentials
knife[:openstack_username] = "admin"
knife[:openstack_password] = "openstackPassword"
knife[:openstack_tenant] = "projectName"
knife[:openstack_auth_url] ="https://nebula_auth_ip:8770/v2.0/tokens"