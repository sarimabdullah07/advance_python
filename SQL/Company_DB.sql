-- CREATE DATABASE Company_Record--
-- SHOW DATABASES;
-- CREATE database IF NOT EXISTS Company;

use company;
/*
orders
orderid
cut_name
city default values
product_name
price
qty
order time
order_year YEAR
*/
/*
CREATE table orders(

order_id INT auto_increment primary key,
product_name varchar(50) not null,
customer_name varchar(70) not null,
city varchar(40) not null default "Mumbai",
price decimal(10,2) not null,
qty smallint not null,
order_year YEAR,
order_time timestamp default current_timestamp
);
*/
-- show tables
describe orders;
-- insert into orders(product_name,customer_name,city,price,qty,order_year,order_time) values("Xiaomi","Abdullah","Aurangabaad","29730",2,2026,"2026-11-25 20:20:30");
-- insert into orders(product_name,customer_name,city,price,qty,order_year,order_time) values("Samsung","Hanzala","Delhi","23782",1,2026,"2026-11-25 20:24:39");
-- insert into orders(product_name,customer_name,city,price,qty,order_year,order_time) values("OPPO","Mahmood","Pune","19500",3,2026,"2026-11-26 20:13:59");
-- insert into orders(product_name,customer_name,city,price,qty,order_year,order_time) values("Apple","Qasim","Nashik","67900",3,2026,"2026-11-26 20:20:39");
insert into orders(product_name,customer_name,price,qty,order_year) values("Apple","Razique","67900",3,2026);

select * from orders;