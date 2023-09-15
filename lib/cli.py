from db.models import Base, User, Contact
from helpers import clear_screen, welcome_banner, exit_app

import time
import maskpass
import sys
from db.hash import hash_password

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from simple_term_menu import TerminalMenu
from prettycli import red, green, blue, yellow

engine = create_engine("sqlite:///db/user_contacts.db")
Session = sessionmaker(bind=engine)
session = Session()


def start():
    clear_screen(20)
    welcome_banner()
    app_start_termical()


def app_start_termical():
    print(green("Please selection from below options in order to proceed further."))
    options = ["Sign Up", "Login", "Exit"]
    terminal_menu = TerminalMenu(
        options,
        menu_cursor_style=(
            "fg_cyan",
            "bold",
        ),
        menu_highlight_style=(
            "fg_cyan",
            "standout",
        ),
    )
    selection = terminal_menu.show()

    if selection == 0:
        sign_up()
    elif selection == 1:
        handle_login()
    else:
        exit_app()


def sign_up():
    print(blue("Please input required details in order to Sign up for App."))

    username = input("Enter Username: ")
    password = hash_password(maskpass.askpass())
    # mask password while user enter and convert it to hash
    email = input("Enter Your email: ")
    user = User(username=username, password=password, email=email)

    session.add(user)
    session.commit()
    print(yellow("Thank you for SignUp. Please Login now.."))
    handle_login()


def handle_login():
    print(yellow("Please Enter Username and password to Login."))
    username = input("Username: ")
    password = hash_password(maskpass.askpass())
    user = session.query(User).filter_by(username=username, password=password).first()

    if user:
        render_home_page(user)
    else:
        print(red("Invalid credentials Entered. Redirecting to start Terminal..."))
        time.sleep(2)
        # if wrong credentials then user need to go back to main page for signup, login or exit
        start()


def render_home_page(user):
    clear_screen(20)
    print(green(f"Welcome {user.username}"))
    user_home_page(user)


def user_home_page(user):
    print(yellow("Please choose from below options : "))
    options = [
        "View all contacts",
        "Search contact",
        "Edit contact",
        "Delete contact",
        "Add new contact",
        "Logout",
    ]
    terminal_menu = TerminalMenu(options)
    choice = terminal_menu.show()
    if choice == 0:
        view_all_contacts(user)
    elif choice == 1:
        search_contact(user)
    elif choice == 2:
        edit_contact(user)
    elif choice == 3:
        delete_contact(user)
    elif choice == 4:
        add_new_contact(user)
    elif choice == 5:
        log_out()


def view_all_contacts(user):
    clear_screen(5)
    contacts = session.query(Contact).filter_by(user=user).all()
    if not contacts:
        print(red("No contacts found. Go to home page for more options."))
        go_back_logout(user)
    else:
        for contact in contacts:
            show_contact(contact)
        print(yellow(f"Total {len(contacts)} contacts are found: "))
        go_back_logout(user)


def show_contact(contact):
    print(green(f"< Contact ID : {contact.id}"))
    print(green(f"   Name : {contact.name}"))
    print(green(f"   Phone: {contact.phone}"))
    print(green(f"   Email: {contact.email}"))
    print(green(f"   Category: {contact.category}"))
    print(green(f"   Address: {contact.address} >\n"))


# common function for searching contacts by name
def search_contact_by_name(user, search):
    contacts = (
        session.query(Contact)
        .filter_by(user=user)
        .filter(Contact.name.ilike(f"%{search}%"))
        .all()
    )
    return contacts


def search_contact(user):
    search = input("Enter a name to search for contact details: ")
    contacts = search_contact_by_name(user, search)

    if not contacts:
        print(red(f"No contacts found for '{search}'."))
        go_back_logout(user)
    else:
        print(green(f"Total {len(contacts)} contacts are found for {search}:"))
        for contact in contacts:
            show_contact(contact)
        go_back_logout(user)


def edit_contact(user):
    search = input("Enter a name of the contact you want to edit: ")
    contacts = search_contact_by_name(user, search)
    if not contacts:
        print(
            red(f"No contacts found for '{search}'. Go to Home page for more options")
        )
        go_back_logout(user)
    else:
        id_captured = []
        for contact in contacts:
            show_contact(contact)
            id_captured.append(contact.id)
        contact_id = int(input("Enter the ID of the contact you want to edit: "))
        if contact_id in id_captured:
            contact_to_be_edited = (
                session.query(Contact).filter_by(id=contact_id, user=user).first()
            )
            field = input(
                "Enter the field you want to edit (name/phone/email/category/address): "
            ).lower()
            new_value = input(f"Enter the new {field}: ")

            setattr(contact_to_be_edited, field, new_value)
            session.commit()
            print(green(f"Contact detail for {search} updated successfully."))
            go_back_logout(user)
        else:
            print(
                red(
                    "Incorrect id entered. Please go back to home page for more options."
                )
            )
            go_back_logout(user)


def delete_contact(user):
    search = input("Enter a name of the contact you want to delete: ")
    contacts = search_contact_by_name(user, search)
    if not contacts:
        print(
            red(f"No contacts found for '{search}'. Go to home page for more options")
        )
        go_back_logout(user)
    else:
        print(green(f"Total {len(contacts)} contacts are found for {search}."))
        id_captured = []
        for contact in contacts:
            show_contact(contact)
            id_captured.append(contact.id)

        contact_id = int(input("Enter the ID of the contact you want to delete: "))

        if contact_id in id_captured:
            contact_to_be_deleted = (
                session.query(Contact).filter_by(id=contact_id, user=user).first()
            )
            session.delete(contact_to_be_deleted)
            session.commit()
            print(green(f"Contact detail for {search} deleted successfully."))
            go_back_logout(user)
        else:
            print(
                red(
                    "Incorrect id entered. Please go back to home page for more options."
                )
            )
            go_back_logout(user)


def add_new_contact(user):
    print(yellow("Enter required details to add new contact."))
    name = input("Name: ")
    phone = input("Phone: ")
    email = input("Email: ")
    category = input("Category, choose from (work/family/friend/other): ")
    address = input("Address: ")

    new_contact = Contact(
        name=name,
        phone=phone,
        email=email,
        category=category,
        address=address,
        user=user,
    )
    session.add(new_contact)
    session.commit()
    print(green("New contact added successfully. Showing new contact : "))
    show_contact(new_contact)
    go_back_logout(user)


# common function for user to go to home page or logout after each action
def go_back_logout(user):
    user_choice = input(red("Enter b to go back to Home page or l to logout : "))
    if user_choice.lower() == "b":
        user_home_page(user)
    elif user_choice.lower() == "l":
        log_out()
    else:
        print(red("Please enter valid input in order to procees further !!"))
        go_back_logout(user)


def log_out():
    print("You are successfully logout from app. Thanks for Using Contact Storage App.")
    print("Redirecting to start Terminal...")
    time.sleep(1)
    app_start_termical()


start()
