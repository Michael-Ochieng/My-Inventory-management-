DROP DATABASE if exists stock;
CREATE DATABASE stock;
USE stock;
DROP TABLE if exists product;
CREATE table product(prname varchar(50),prcode varchar(10), quantity int);
DROP TABLE if exists sales;
CREATE table product(prname varchar(50),prcode varchar(10), quantity int);
DROP table if exists staff;
CREATE table staff(name varchar(50),regno varchar(10), phone_no int);
COMMIT