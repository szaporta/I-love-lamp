# This sets up a LAMP stack for you in Ubuntu (I used Ubuntu Xenial - 16.04)

# Install Apache
apt-get install apache2 -y

# Install PHP
apt-get install php7.0 php7.0-cli libapache2-mod-php7.0 php-mcrypt php-mysql -y

# Install MySQL
apt-get install mysql-client mysql-server -y

# Harden MySQL security - not necessary at the moment
# mysql_secure_installation   

# Upload the data to the database
mysql -uroot -pdemodog mysql < world.sql

# Install curl
apt-get install curl -y

# Set up the dd-agent + MySQL integration
bash agent_install.sh
