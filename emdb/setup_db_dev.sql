-- Create database emdb_db
CREATE DATABASE IF NOT EXISTS emdb_db;
USE emdb_db;
CREATE USER IF NOT EXISTS 'emdb_dev'@'localhost' IDENTIFIED BY 'emdb_dev_pwd';
GRANT ALL PRIVILEGES ON `emdb_db`.* TO 'emdb_dev'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'emdb_dev'@'localhost';
FLUSH PRIVILEGES;
