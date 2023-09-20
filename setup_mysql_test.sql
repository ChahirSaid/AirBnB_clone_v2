-- Create the database if it doesn't already exist
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- Create the user if it doesn't already exist
-- Set the password for the new user
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- Grant all privileges on the new database to the new user
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

-- Apply changes immediately
FLUSH PRIVILEGES;

-- Grant SELECT privilege on the performance_schema database to the new user
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';

-- Apply changes immediately
FLUSH PRIVILEGES;
