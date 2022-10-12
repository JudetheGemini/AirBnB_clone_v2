-- SQL script that sets up Development server

-- Create a database hbnb_dev_db
CREATE DATABASE IF NOT EXISTS `hbnb_dev_db`;

-- Create user hbnb_dev
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- Grant user hbnb_dev all privileges
GRANT ALL PRIVILEGES on `hbnb_dev_db`.* TO 'hbnb_dev'@'localhost';

--Grant user hbnb_dev SELECT privileges on 'performance_schema'
GRANT SELECT on `performance_schema`.* TO 'hbnb_dev'@'localhost';
