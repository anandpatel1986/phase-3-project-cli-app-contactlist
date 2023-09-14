from db.models import Base, User, Contact
import time
import maskpass
import sys
from db.hash import hash_password
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from simple_term_menu import TerminalMenu
from prettycli import red

engine = create_engine("sqlite:///db/user_contacts.db")
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()


def start():
    clear_screen(10)

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
    print("Please input details in order to Sign up for App.")

    username = input("Enter Username: ")
    password = hash_password(maskpass.askpass())
    # mask password while user enter and convert it to hash
    email = input("Enter Your email: ")
    user = User(username=username, password=password, email=email)

    # session.add(user)
    # session.commit()
    # session.close()
    print("Thank you for SignUp. Please Login now..")
    handle_login()


def handle_login():
    print("Please Enter Username and password to Login.")
    username = input("Username: ")
    password = hash_password(maskpass.askpass())
    user = session.query(User).filter_by(username=username, password=password).first()
    session.close()

    if user:
        print("Loading main page after login.")
    else:
        print("Invalid credentials Entered. Please start again...")
        time.sleep(2)
        # if wrong credentials then user need to go back to main page for signup or login or exit
        start()


def exit():
    print("Exiting from app. Thanks for using Contact Storage App. Bye !!!")
    time.sleep(2)
    sys.exit()


start()
