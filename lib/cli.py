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
    choice = terminal_menu.show()

    if choice == 0:
        sign_up()
    elif choice == 1:
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
        render_home_page(user)
    else:
        print("Invalid credentials Entered. Please start again...")
        time.sleep(2)
        # if wrong credentials then user need to go back to main page for signup or login or exit
        start()


def render_home_page(user):
    clear_screen(10)
    print(f"Welcome {user.username}")
    print("Please choose from below options : ")
    options = ["View all contacts", "Search contact", "Add new contact", "Logout"]
    terminal_menu = TerminalMenu(options)
    choice = terminal_menu.show()
    if choice == 0:
        view_all_contacts(user)
    elif choice == 1:
        search_contact(user)
    elif choice == 2:
        add_new_contact(user)
    elif choice == 3:
        log_out(user)


def view_all_contacts(user):
    pass


def search_contact(user):
    pass


def add_new_contact(user):
    pass


def log_out(user):
    pass


def exit():
    print("Exiting from app. Thanks for using Contact Storage App. Bye !!!")
    time.sleep(2)
    sys.exit()


start()
