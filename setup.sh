# This sets up a LAMP stack for you in Ubuntu (I used Ubuntu 16.04)

# Install Apache
apt-get install apache2 -y

# Install PHP
apt-get install php 7.0 php7.0-cli libapache2-mod-php7.0 php-mcrypt php-mysql -y

# Install MySQL
apt-get install mysql-client mysql-server -y
mysql_secure_installation #be sure to harden your mysql security

# Navigate to the directory with the sample databases in it, for automated loading
cd /sakila-db/

# Upload the sample databases to the database
mysql -u root -plimber  --execute="CREATE DATABASE Sakila; USE Sakila; SOURCE sakila-schema.sql; SOURCE sakila-data.sql;"

# Navigate to web directory for LAMP stack
cd /var/www/html

# Create PHP file to test
echo '<?php phpinfo(); ?>' > info.php
