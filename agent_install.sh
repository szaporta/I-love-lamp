# NOTE: Change API KEY!

# Set up dd-agent on Ubuntu 16.04
DD_API_KEY=API_KEY_GOES_HERE bash -c "$(curl -L https://raw.githubusercontent.com/DataDog/dd-agent/master/packaging/datadog-agent/source/install_agent.sh)"

# Set up MySQL integration - no root pw needed
mysql -u root mysql < dd-user_mysql_setup.sql

# Restart Agent 
sudo /etc/init.d/datadog-agent restart

# Set up mysql.yaml file - copy example file to yaml file
cp /etc/dd-agent/conf.d/mysql.yaml.example /etc/dd-agent/conf.d/mysql.yaml

# Set up apache.yaml file - copy example file to yaml file
cp /etc/dd-agent/conf.d/apache.yaml.example /etc/dd-agent/conf.d/apache.yaml

# Python script to replace certain lines with variables
python yamlread.py 
