create schema dinner;
use dinner;

create table food_type(
    id              INT unsigned auto_increment PRIMARY KEY,
    food_type       VARCHAR(10)
);

create table food(
	id              INT unsigned auto_increment PRIMARY KEY,
	food_type_id    INT comment '음식 카테고리 성격의 칼럼',
	name            VARCHAR(20) unique,
	ingredient      LONGTEXT,
	spice           LONGTEXT,
	recipe          LONGTEXT,
    calorie         INT(5) comment '단위는 cal',
	carbohydrate    INT(5) comment '단위는 g',
	protein         INT(5) comment '단위는 g',
	vitamin         INT(5) comment '단위는 g'
);

insert into food_type(food_type)
values
('반찬'),
('국');

