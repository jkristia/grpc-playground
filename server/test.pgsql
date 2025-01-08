

CREATE TABLE IF NOT EXISTS my_Table2 (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

SELECT * from my_Table2;

SELECT datname FROM pg_database;

CREATE DATABASE my_db

CREATE TABLE IF NOT EXISTS my_db.my_Table (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);


SELECT * from my_Table2;


SELECT 1 FROM pg_database WHERE datname = 'my_dbs'
SELECT * FROM pg_database


DROP DATABASE my_db
DROP DATABASE my_db_take2

