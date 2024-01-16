#!/bin/bash

# MySQL Server Connection Information
MYSQL_USER="your_mysql_user"
MYSQL_PASSWORD="your_mysql_password"
MYSQL_HOST="your_mysql_host"

DB_NAME="hbtn_0c_0"

DB_EXISTS=$(mysql -u$MYSQL_USER -p$MYSQL_PASSWORD -h$MYSQL_HOST -e "SHOW DATABASES LIKE '$DB_NAME';" | grep $DB_NAME)


if [ -z "$DB_EXISTS" ]; then
    mysql -u$MYSQL_USER -p$MYSQL_PASSWORD -h$MYSQL_HOST -e "CREATE DATABASE $DB_NAME;"
    echo "Database $DB_NAME created successfully."
else
    echo "Database $DB_NAME already exists. No action taken."
fi
