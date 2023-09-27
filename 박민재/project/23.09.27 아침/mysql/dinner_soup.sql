drop schema dinner;
create schema dinner;
use dinner;

create table soup(
	id INT unsigned auto_increment PRIMARY KEY,
	name VARCHAR(20) unique,
	ingredient VARCHAR(1000) NOT NULL,
	spice VARCHAR(1000) NOT NULL,
	recipe VARCHAR(1000) NOT NULL,
    calorie varchar(10),
	carbohydrate varchar(10),
	protein varchar(10),
	vitamin varchar(10)
);

insert into soup(name, ingredient, spice, recipe, calorie, carbohydrate, protein, vitamin)
value('미역국','미역','들기름','1','1cal','1g','1g','1g');
insert into soup(name, ingredient, spice, recipe, calorie, carbohydrate, protein, vitamin)
value('계란국','계란','육수','2','2cal','2g','2g','2g');