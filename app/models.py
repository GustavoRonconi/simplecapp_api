from sqlalchemy import Boolean, Column, String, Integer, ForeignKey, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func

import uuid

from .database import Base


class User(Base):
    __tablename__ = "users"

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    email = Column(String, unique=True, index=True)
    phone_number = Column(String)
    state = Column(String)
    city = Column(String)
    zip_code = Column(String)
    district = Column(String)
    street = Column(String)
    number = Column(String)
    is_active = Column(Boolean, default=True)
    legal_person_id = Column(
        UUID(as_uuid=True), ForeignKey("legal_persons.id"), null=True
    )
    natural_person_id = Column(
        UUID(as_uuid=True), ForeignKey("natural_persons.id"), null=True
    )


class LegalPerson(Base):
    __tablename__ = "legal_persons"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    cnpj = Column(String, unique=True, index=True)
    company_name = Column(String)


class NaturalPerson(Base):
    __tablename__ = "natural_persons"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(Integer, ForeignKey("users.id"))
    cpf = Column(String, unique=True, index=True)
    name = Column(String)
