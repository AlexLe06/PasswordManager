from backend.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
import datetime


class User(Base):
    __tablename__ = "User"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password_hash = Column(String, unique=False, nullable=False)
    date_created = Column(datetime, default=datetime.datetime.utcnow)

    vault_entries = relationship("VaultEntry", back_populates="user")

class VaultEntry(Base):
    __tablename__ = "UserEntries"

    id = Column(Integer, primary_key=True)
    website = Column(String, nullable=False)
    username = Column(String, nullable=False)
    password_encrypt = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey=("user.id"), nullable=False)

    user = relationship("User", back_populates="vault_entries")
