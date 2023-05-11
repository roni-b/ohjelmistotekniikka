from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, Table, exc
from sqlalchemy.orm import sessionmaker, relationship, declarative_base
import bcrypt
from config import DATABASE_FILENAME

Base = declarative_base()

association_table = Table('association', Base.metadata,
                          Column('quote_id', Integer, ForeignKey('quotes.id')),
                          Column('user_id', Integer, ForeignKey('users.id'))
                          )

class User(Base):
    """
    Käyttäjäolio, joka edustaa käyttäjää tietokannassa.
    """
    __tablename__ = "users"
    uid = Column("id", Integer, primary_key=True)
    username = Column("username", String, unique=True, nullable=False)
    password = Column("password", String, nullable=False)
    quotes = relationship(
        "Quote", secondary=association_table, back_populates="users")

    def __repr__(self):
        """
        Palauttaa käyttäjän merkkijonoesityksen.
        """
        return f"user: {self.uid} {self.username} {self.password}"

class Quote(Base):
    """
    Lainausolio, joka edustaa lainausta tietokannassa.
    """
    __tablename__ = "quotes"
    qid = Column("id", Integer, primary_key=True)
    content = Column("content", String)
    author = Column("author", String)
    tags = Column("tags", String)
    users = relationship(
        "User", secondary=association_table, back_populates="quotes")

    def __repr__(self):
        return f"quote: {self.qid} {self.content} {self.author} {self.tags}"

engine = create_engine(f"sqlite:///src/model/{DATABASE_FILENAME}")

session_maker = sessionmaker(bind=engine)

def register(username, password):
    """
    Rekisteröi käyttäjän tietokantaan.

    Args:
        username (str): Käyttäjänimi
        password (str): Salasana

    Returns:
        bool: True, jos käyttäjän rekisteröinti onnistui, muuten False.
    """
    password_bytes = password.encode('utf-8')
    password_salt = bcrypt.gensalt()
    password_hash = bcrypt.hashpw(password_bytes, password_salt)
    with session_maker() as session:
        try:
            session.add(User(username=username, password=password_hash))
            session.commit()
            return True
        except exc.IntegrityError:
            session.rollback()
            return False

def login(username, password):
    """
    Kirjaa käyttäjän sisään tietokantaan.

    Args:
        username (str): Käyttäjänimi
        password (str): Salasana

    Returns:
        bool: True, jos käyttäjän kirjautuminen onnistui, muuten False.
    """
    password_bytes = password.encode('utf-8')
    with session_maker() as session:
        user = session.query(User).filter_by(username=username).first()
        return user and bcrypt.checkpw(password_bytes, user.password)

def show_user(username):
    """
    Palauttaa käyttäjän tiedot.

    Args:
        username (str): Käyttäjänimi

    Returns:
        dict or False: Käyttäjän tiedot sanakirjana tai False, jos käyttäjää ei ole.
    """
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
    """Lisää uuden lainauksen tietokantaan käyttäjänimellä ja lainauksella.

    Args:
        username (str): käyttäjänimi
        quote (tuple): uusi lainaus muodossa (sisältö, kirjoittaja, tunnisteet)

    Returns:
        bool: Palauttaa True, jos lainaus lisättiin tietokantaan onnistuneesti,
              None jos lainaus löytyy jo tietokannasta tai False jos käyttäjää ei löydy.
    """
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
    """Poistaa käyttäjän tietokannasta käyttäjänimen perusteella.

    Args:
        username (str): käyttäjänimi

    Returns:
        bool: Palauttaa True, jos käyttäjä poistettiin tietokannasta onnistuneesti,
              False jos käyttäjää ei löydy.
    """
    with session_maker() as session:
        user = session.query(User).filter_by(username=username).first()
        if user:
            session.delete(user)
            session.commit()
            return True
        return False

def delete_quote(content):
    """Poistaa lainauksen tietokannasta lainauksen sisällön perusteella.

    Args:
        content (str): lainauksen sisältö

    Returns:
        bool: Palauttaa True, jos lainaus poistettiin tietokannasta onnistuneesti,
              False jos lainausta ei löydy.
    """
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
