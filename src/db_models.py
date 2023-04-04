from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, CHAR, UniqueConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    uid = Column("id", Integer, primary_key=True)
    username = Column("username", String, unique=True, nullable=False)
    password = Column("password", String, nullable=False)

    def __init__(self, uid, username, password):
        self.uid = uid
        self.username = username
        self.password = password
    
    def __repr__(self):
        return f"{self.uid} {self.username} {self.password}"
    
class Quote(Base):
    __tablename__ = "quotes"
    qid = Column("id", Integer, primary_key=True)
    content = Column("content", String)
    author = Column("author", String)
    tags = Column("tags", String)

    def __init__(self, qid, content, author, tags):
        self.qid = qid
        self.content = content
        self.author = author
        self.tags = tags
    
    def __repr__(self):
        return f"{self.qid} {self.content} {self.author} {self.tags}"

# engine = create_engine("sqlite:///mydb.db", echo=True)

# Base.metadata.create_all(bind=engine)

# Session = sessionmaker(bind=engine)
# session = Session()

# user = User(1, "aku", "salasana")
# session.add(user)
# session.commit()

# user2 = User(2, "mikki", "salasana")
# user3 = User(3, "roope", "salasana")
# user4 = User(4, "iines", "salasana")

# session.add(user2)
# session.add(user3)
# session.add(user4)
# session.commit()

# users = session.query(User).all()
# print(users)

# from datetime import datetime

# from sqlalchemy import Column, Integer, String, DateTime, create_engine

# from sqlalchemy.orm import declarative_base, sessionmaker

# Base = declarative_base()

# class UserModel(Base):
#     __tablename__ = 'user'
#     id = Column(Integer, primary_key=True)
#     name = Column(String, nullable=False)
#     created = Column(DateTime, default=datetime.utcnow)

# engine = create_engine("sqlite:///mydb.db", echo=True)

# Base.metadata.create_all(bind=engine)

# Session = sessionmaker(bind=engine)
# session = Session()