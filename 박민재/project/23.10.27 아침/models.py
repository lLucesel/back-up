class food_type(Base):
    __tablename__ = "food_type"

    id = Column(int, primary_key = True, index = True)
    food_type = Column(str)

class food(Base):
    __tablename__ = "food"

