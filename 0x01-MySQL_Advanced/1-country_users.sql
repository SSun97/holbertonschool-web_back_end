-- Write a SQL script that creates a table users following these requirements:
CREATE TABLE IF NOT EXISTS USERS (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255),
    country ENUM("US", "CO", "IN") DEFAULT "US" NOT NULL
);