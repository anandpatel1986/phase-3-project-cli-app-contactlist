from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, Integer, String, ForeignKey

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    password = Column(String(15), nullable=False)
    email = Column(String(50))
    contacts = relationship("Contact", back_populates="user")

    def __repr__(self):
        return f"Username: {self.username}, email: {self.email}"


class Contact(Base):
    __tablename__ = "contacts"

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    phone = Column(String(15))
    email = Column(String(50))
    category = Column(String, nullable=False)
    address = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="contacts")

    def __repr__(self):
        return (
            f"Contact Details of : {self.name}"
            + f"Phone: {self.phone}"
            + f"email : {self.email}"
            + f"category : {self.category}"
            + f"Address: {self.address}"
        )
