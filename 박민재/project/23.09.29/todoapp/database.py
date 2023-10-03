from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

#SQLALCHEMY_DATABASE_URL = "sqlite:///./todos.db"
#SQLALCHEMY_DATABASE_URL = "postgresql://{사용자이름}:{사용자패스워드}@{host}/{database}"
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://{사용자이름}:{사용자패스워드}@{host}/{database}"

#engine = create_engine(
#	SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
#)
engine = create_engine(
	SQLALCHEMY_DATABASE_URL
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


Base = declarative_base()