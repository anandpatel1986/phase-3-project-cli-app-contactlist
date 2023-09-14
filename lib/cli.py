from db.models import Base, User, Contact

# from db.hash import hash_password
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from simple_term_menu import TerminalMenu
from prettycli import red

engine = create_engine("sqlite:///db/user_contacts.db")
# Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()


def start():
    clear_screen(30)

    print(red("Welcome to Contact storage App"))
    options = ["Sign Up", "Login", "Exit"]
    terminal_menu = TerminalMenu(options)
    menu_entry_index = terminal_menu.show()


def clear_screen(lines):
    print("\n" * lines)


start()
