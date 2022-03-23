from sqlalchemy import Boolean, Column, String, ForeignKey, DateTime
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
    phone_number = Column(String, nullable=True)
    state = Column(String, nullable=True)
    city = Column(String, nullable=True)
    zip_code = Column(String, nullable=True)
    district = Column(String, nullable=True)
    street = Column(String, nullable=True)
    number = Column(String, nullable=True)
    is_active = Column(Boolean, default=True)
    legal_person_id = Column(
        UUID(as_uuid=True), ForeignKey("legal_persons.id"), nullable=True
    )
    natural_person_id = Column(
        UUID(as_uuid=True), ForeignKey("natural_persons.id"), nullable=True
    )


class LegalPerson(Base):
    __tablename__ = "legal_persons"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    cnpj = Column(String, unique=True, index=True, nullable=True)
    company_name = Column(String, nullable=True)


class NaturalPerson(Base):
    __tablename__ = "natural_persons"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    cpf = Column(String, unique=True, index=True, nullable=True)
    name = Column(String, nullable=True)
