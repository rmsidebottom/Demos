#!/bin/bash

user="root"
pass="password"
db="demo"
table="users"

mysql -u$user -p$pass -e "create database if not exists $db"
mysql -u$user -p$pass -D$db -e "create table if not exists users(username varchar(20), password varchar(50), primary key(username) );"
mysql -u$user -p$pass -D$db -e "insert into users (username, password) values (\"csec\", \"cybersecurity\"), (\"johnny\", \"superHARDpassw0rdTOcrack\"), (\"dave\", \"password\");"

