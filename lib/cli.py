from db.models import Base, User, Contact
from helpers import clear_screen, exit_app, welcome_banner
import time
import maskpass
import sys
from db.hash import hash_password
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from simple_term_menu import TerminalMenu
from prettycli import red, green

engine = create_engine("sqlite:///db/user_contacts.db")
Session = sessionmaker(bind=engine)
session = Session()


def start():
    clear_screen(20)
    welcome_banner()

    options = ["Sign Up", "Login", "Exit"]
    terminal_menu = TerminalMenu(options)
    choice = terminal_menu.show()

    if choice == 0:
        sign_up()
    elif choice == 1:
        handle_login()
    else:
        exit_app()


def sign_up():
    print("Please input details in order to Sign up for App.")

    username = input("Enter Username: ")
    password = hash_password(maskpass.askpass())
    # mask password while user enter and convert it to hash
    email = input("Enter Your email: ")
    user = User(username=username, password=password, email=email)

    session.add(user)
    session.commit()
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
        render_home_page(user)
    elif choice == 1:
        search_contact(user)
    elif choice == 2:
        edit_contact(user)
    elif choice == 3:
        delete_contact(user)
    elif choice == 4:
        add_new_contact(user)
    elif choice == 5:
        log_out(user)


def view_all_contacts(user):
    contacts = session.query(Contact).filter_by(user=user).all()
    if not contacts:
        print("No contacts found.")
        return
    for contact in contacts:
        show_contact(contact)


def show_contact(contact):
    print(green(f"< Contact ID : {contact.id}"))
    print(f"   Name : {contact.name}")
    print(f"   Phone: {contact.phone}")
    print(f"   Email: {contact.email}")
    print(f"   Category: {contact.category}")
    print(f"   Address: {contact.address} >\n")


def search_contact(user):
    search = input("Enter a name to search for details: ")
    contacts = (
        session.query(Contact)
        .filter_by(user=user)
        .filter(Contact.name.ilike(f"%{search}%"))
        .all()
    )
    if not contacts:
        print(f"No contacts found for '{search}'.")
        time.sleep(2)
        return
    for contact in contacts:
        show_contact(contact)


def edit_contact(user):
    search = input("Enter a name of the contact you want to edit: ")
    contacts = (
        session.query(Contact)
        .filter_by(user=user)
        .filter(Contact.name.ilike(f"%{search}%"))
        .all()
    )
    if not contacts:
        print("Contact not found.")
        time.sleep(2)
        return
    for contact in contacts:
        show_contact(contact)
    contact_id = input("Enter the ID of the contact you want to edit: ")
    contact_to_be_edited = (
        session.query(Contact).filter_by(id=contact_id, user=user).first()
    )

    field = input(
        "Enter the field you want to edit (name/phone/email/category/address): "
    ).lower()
    new_value = input(f"Enter the new {field}: ")

    setattr(contact_to_be_edited, field, new_value)
    session.commit()
    print("Contact updated successfully. Redirecting to Home page...")
    time.sleep(2)
    render_home_page(user)


def delete_contact(user):
    search = input("Enter a name of the contact you want to delete: ")
    contacts = (
        session.query(Contact)
        .filter_by(user=user)
        .filter(Contact.name.ilike(f"%{search}%"))
        .all()
    )
    if not contacts:
        print("Contact not found.")
        time.sleep(2)
        return
    for contact in contacts:
        show_contact(contact)
    contact_id = input("Enter the ID of the contact you want to delete: ")
    contact_to_be_deleted = (
        session.query(Contact).filter_by(id=contact_id, user=user).first()
    )
    session.delete(contact_to_be_deleted)
    session.commit()
    print("Contact deleted successfully. Redirecting to Home page...")
    time.sleep(2)
    render_home_page(user)


def add_new_contact(user):
    print("Enter required details to add new contact.")
    name = input("Name: ")
    phone = input("Phone: ")
    email = input("Email: ")
    category = input("Category from (work/family/friend/other): ")
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
    show_contact(new_contact)
    print("New contact added successfully. Redirecting to Home page...")
    time.sleep(2)
    render_home_page(user)


def log_out(user):
    print("You are successfully logout from app. Thanks for Using Contact Storage App.")
    time.sleep(3)
    start()


start()
