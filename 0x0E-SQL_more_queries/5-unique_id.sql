--Script for table creation.
--Query to establish the 'unique_id' table in the MySQL server.
CREATE TABLE IF NOT EXISTS unique_id (
       id INT UNIQUE DEFAULT 1,
       name VARCHAR(256));
