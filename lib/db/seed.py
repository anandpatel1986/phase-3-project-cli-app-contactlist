from faker import Faker
import random

from hash import hash_password
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import User, Contact

engine = create_engine("sqlite:///user_contacts.db")
Session = sessionmaker(bind=engine)
session = Session()

session.query(User).delete()
session.query(Contact).delete()

fake = Faker()

# Create 3 users
users = []
for _ in range(3):
    username = fake.user_name()
    password = hash_password(fake.password())
    email = fake.email()
    user = User(username=username, password=password, email=email)
    session.add(user)
    users.append(user)
session.commit()

# Create 10 contacts for each users
for user in users:
    for _ in range(10):
        contact = Contact(
            name=fake.name(),
            phone=fake.phone_number(),
            email=fake.email(),
            category=random.choice(["Work", "Family", "Friend", "Other"]),
            address=fake.address(),
            user=user,
        )
        session.add(contact)
session.commit()
print("Sample data seeded successfully.")
