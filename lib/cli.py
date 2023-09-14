from db.models import Base, User, Contact
import time
import sys

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

    if options[menu_entry_index] == "Sign Up":
        sign_up()
    elif options[menu_entry_index] == "Login":
        handle_login()
    else:
        exit()


def clear_screen(lines):
    print("\n" * lines)


def sign_up():
    pass


def handle_login():
    pass


def exit():
    print("Exiting from app. Thanks for using Contact Storage App. Bye !!!")
    time.sleep(2)
    sys.exit()


start()
