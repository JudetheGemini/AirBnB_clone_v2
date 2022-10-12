-- Script that prepares a MySQL server for the project

-- create database hbnb_test_db
CREATE DATABASE IF NOT EXISTS `hbnb_test_db`;

-- create user hbnb_test
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- assign user privileges
GRANT ALL PRIVILEGES ON `hbnb_test_db`.* TO 'hbnb_test'@'localhost';

-- assign privileges to performance_schema DB
GRANT SELECT ON `performance_schema`.* TO 'hbnb_test'@'localhost';
