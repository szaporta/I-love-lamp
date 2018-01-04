# I-love-lamp

NOTE: DO THIS AS SUDO
1. Run apt-get update
2. Run apt install git
3. Run git clone https://github.com/szaporta/I-love-lamp.git
4. Be sure to put your API key in the "agent_install.sh" file
5. Run setup.sh

This installs a LAMP stack (Linux, Apache, MySQL, PHP) very quickly, with no root pw, installs the dd-agent, creates the datadog user in MySQL, copies the "mysql.yaml.example" file, strips the ".example" from the file, and modifies it, so that the user and password are populated, and the MySQL integration works OOTB.
