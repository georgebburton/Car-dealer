use cars;
drop table if exists car;
create table car(
	id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
    year varchar(5) not null ,
    make varchar(20) not null ,
    model varchar(20) not null,
    stock INT
    );
