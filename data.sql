create database taskmanager;
use taskmanager;

create table Accounts(
    Email varchar(80) primary key,
    passwords varchar(80) not null
);

select * from Accounts;
