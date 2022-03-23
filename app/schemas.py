from pydantic import BaseModel
from typing import Optional


class BasicUser(BaseModel):
    email: str

    class Config:
        orm_mode = True


class LegalPerson(BaseModel):
    cnpj: Optional[str]
    company_name: Optional[str]

    class Config:
        orm_mode = True


class NaturalPerson(BaseModel):
    cpf: Optional[str]
    name: Optional[str]

    class Config:
        orm_mode = True


class User(BasicUser, BaseModel):
    phone_number: Optional[str]
    state: Optional[str]
    city: Optional[str]
    zip_code: Optional[str]
    district: Optional[str]
    street: Optional[str]
    number: Optional[str]
    legal_person: Optional[LegalPerson] = None
    natural_person: Optional[NaturalPerson] = None
