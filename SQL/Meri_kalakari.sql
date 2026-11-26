-- create database if not exists Student_Records;
-- show databases;
use Student_Records;
/*
create table marks_records(
serial_no INT auto_increment primary key,
Roll_no INT,
name varchar(70),
city varchar(40) not null default "Mumbai",
phy tinyint,
chem tinyint,
math tinyint,
percent decimal(6,2),
remark char(1),
date timestamp default current_timestamp
);
*/
show tables;
describe marks_records;

insert into marks_records(Roll_no,name,city,phy,chem,math,percent,remark) values(10,"Alice","Pune","90","85","80","85","A+");
select * from marks_records;
