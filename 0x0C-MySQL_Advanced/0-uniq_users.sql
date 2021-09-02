-- creates a table users
-- where: the script should not fail if the table already exists
-- this script can be executed on any database

CREATE TABLE
IF NOT EXISTS users (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255)
);
