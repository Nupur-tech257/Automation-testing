
CREATE TABLE if not exists users(
id int(11) PRIMARY KEY NOT NULL,
name varchar(255) NOT NULL,
email varchar(255) NOT NULL
);

TRUNCATE TABLE users;

INSERT INTO users 
VALUES ( 3,'hey','hey@gmail.com');