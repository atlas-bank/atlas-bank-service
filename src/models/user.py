from dataclasses import dataclass

from exceptions.exceptions import BadRequestException
from interfaces.entities_interface import IEntity


@dataclass
class User(IEntity):
    @classmethod
    def get_collection(cls):
        return "users"

    def __init__(
            self,
            full_name: str,
            cpf: str,
            birth_date: str,
            parent_name: str,
            rg: str,
            rg_issuer: str,
            rg_state: str,
            email: str,
            phone: str,
            nationality: str,
            marital_status: str,
            gender: str,
            zip_code: str,
            address: str,
            state: str,
            country: str,
            occupation: str = "",
            salary: str = ""
    ):
        # Required fields
        self.full_name = full_name
        self.cpf = cpf
        self.cpf_validator()

        self.birth_date = birth_date
        self.parent_name = parent_name
        self.rg = rg
        self.rg_issuer = rg_issuer
        self.rg_state = rg_state
        self.email = email
        self.phone = phone
        self.nationality = nationality
        self.marital_status = marital_status
        self.gender = gender
        self.zip_code = zip_code
        self.address = address
        self.state = state
        self.country = country

        # Campos opcionais
        self.occupation = occupation
        self.salary = salary

    def cpf_validator(self):
        if not len(self.cpf) == 11 and not self.cpf.isdigit() and not self.cpf != "00000000000":
            raise BadRequestException("Invalid CPF!")

    def to_dict(self):
        return self.__dict__
