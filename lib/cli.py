from db.models import Base, User, Contact

# from db.hash import hash_password
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# from prettycli import Menu

engine = create_engine("sqlite:///db/user_contacts.db")
# Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()


def start():
    clear_screen(40)
    print("App start")


def clear_screen(lines):
    print("\n" * lines)


start()
