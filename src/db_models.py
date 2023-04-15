from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, Table, exc
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()

association_table = Table('association', Base.metadata,
                          Column('quote_id', Integer, ForeignKey('quotes.id')),
                          Column('user_id', Integer, ForeignKey('users.id'))
                          )

class User(Base):
    __tablename__ = "users"
    uid = Column("id", Integer, primary_key=True)
    username = Column("username", String, unique=True, nullable=False)
    password = Column("password", String, nullable=False)
    quotes = relationship(
        "Quote", secondary=association_table, back_populates="users")

    def __repr__(self):
        return f"user: {self.uid} {self.username} {self.password}"

class Quote(Base):
    __tablename__ = "quotes"
    qid = Column("id", Integer, primary_key=True)
    content = Column("content", String)
    author = Column("author", String)
    tags = Column("tags", String)
    users = relationship(
        "User", secondary=association_table, back_populates="quotes")

    def __repr__(self):
        return f"quote: {self.qid} {self.content} {self.author} {self.tags}"

engine = create_engine('sqlite:///mydb.db', echo=True)

session_maker = sessionmaker(bind=engine)

def register(username, password):
    with session_maker() as session:
        try:
            session.add(User(username=username, password=password))
            session.commit()
            return True
        except exc.IntegrityError:
            session.rollback()
            return False

def login(username, password):
    with session_maker() as session:
        user = session.query(User).filter_by(username=username).first()
        return user and user.password == password

def show_user(username):
    with session_maker() as session:
        user = session.query(User).filter_by(username=username).first()
        if user:
            quotes = []
            for quote in user.quotes:
                quotes.append({'id':quote.qid,
                                'content': quote.content,
                                'author': quote.author,
                                'tags': quote.tags})
            return {'uid': user.uid, 'username': user.username, 'quotes': quotes}
        return False

def add_quote(username, quote):
    with session_maker() as session:
        test = session.query(Quote).filter_by(content=quote[1]).first()
        if test:
            return None
        user = session.query(User).filter_by(username=username).first()
        new_quote = Quote(content=quote[0], author=quote[1], tags=quote[2])
        user.quotes.append(new_quote)
        session.add(new_quote)
        session.commit()
        return True

def delete_user(username):
    with session_maker() as session:
        user = session.query(User).filter_by(username=username).first()
        if user:
            session.delete(user)
            session.commit()
            return True
        return False

def delete_quote(content):
    with session_maker() as session:
        quote = session.query(Quote).filter(Quote.content == content).first()
        if quote:
            session.delete(quote)
            session.commit()
            return True
        return False

def initialize_database():
    Base.metadata.create_all(engine)

if __name__ == '__main__':
    initialize_database()
