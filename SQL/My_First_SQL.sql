-- Creating database for Paras Book Ltd --

-- CREATE DATABASE Paras_Book_Ltd
-- SHOW databases
/*
USE Paras_Book_Ltd; 
CREATE TABLE book_data(
book_id INT,
book_title VARCHAR(50),
Author VARCHAR(30),
year_publish INT,
Publisher INT,
price DECIMAL(10,2)
);
*/

SHOW tables; 
DESCRIBE book_data;

insert into book_data(book_id, book_title, Author, year_publish, Publisher, price) values(103, The_Alchemist, Paul_Charlio, 2013, Santiago, 320.64);
SELECT * from book_data;