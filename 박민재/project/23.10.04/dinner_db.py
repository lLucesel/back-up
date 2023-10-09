from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class FoodType(Base):
    __tablename__ = 'food_type'
    id = Column(Integer, primary_key=True, index=True)
    food_type = Column(String(10), unique=True, index=True)


class Food(Base):
    __tablename__ = 'food'
    id = Column(Integer, primary_key=True, index=True)
    food_type_id = Column(Integer, index=True)
    name = Column(String(20), unique=True, index=True)
    ingredient = Column(Text)
    spice = Column(Text)
    recipe = Column(Text)
    calorie = Column(Integer)
    carbohydrate = Column(Integer)
    protein = Column(Integer)
    vitamin = Column(Integer)


user_name = "admin_mj"
user_pwd = "77gundam77"
db_host = "127.0.0.1"
db_name = "dinner_db"

DATABASE_URL = f"mysql://{user_name}:{user_pwd}@{db_host}/{db_name}?charset=utf8"

engine = create_engine(
    DATABASE_URL,
    charset="utf-8",
    echo=True
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
