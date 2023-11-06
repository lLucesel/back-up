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
INSERT INTO food(food_type_id, name, ingredient, spice, recipe, calorie, carbohydrate, protein, vitamin)
VALUES
('2','오뎅국','오뎅', '멸치액젓', '오뎅을 넣고 끓인다', '44', '44', '44', '44'),
('1','오이소박이','오이', '고추가루', '무야호무야호무야호', '33', '33', '33', '33'),
('2','미역국','미역', '들기름', '무야호무야호무야호', '1', '1', '1', '1'),
('2','계란국','계란', '육수', '무야호무야호', '2', '2', '2', '2'),
('1','고등어갈비구이','고등어', '고추장', '무야호', '11', '11', '11', '11'),
('1','간장목살구이','목살', '간장', '무야호무양호', '22', '22', '22', '22');


