# NOTE: Change API KEY!

# Set up dd-agent on Ubuntu 16.04
DD_API_KEY=d5ed33bc1830f93767bbc1a16056ca95 bash -c "$(curl -L https://raw.githubusercontent.com/DataDog/dd-agent/master/packaging/datadog-agent/source/install_agent.sh)"

# Set up MySQL integration
mysql -u root -plimber User < dd-user_mysql_setup.sql

# Restart Agent 
sudo /etc/init.d/datadog-agent restart
