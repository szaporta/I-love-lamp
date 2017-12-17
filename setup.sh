# This sets up a LAMP stack for you in Ubuntu (I used Ubuntu Xenial - 16.04)

# Install Apache
apt-get install apache2 -y

# Install PHP
apt-get install php7.0 php7.0-cli libapache2-mod-php7.0 php-mcrypt php-mysql -y

# Install MySQL
apt-get install mysql-client mysql-server -y

# Harden MySQL security
mysql_secure_installation

# Navigate to the directory with the sample databases in it, for automated loading
cd sakila-db

# Create the Sakila database
mysql -uroot -plimber  --execute="CREATE DATABASE Sakila;"

# Upload the schema for the Sakila database
mysql -uroot -plimber Sakila < sakila-schema.sql

# Upload the data for the Sakila database
mysql -uroot -plimber Sakila < sakila-data.sql
