from exceptions.exceptions import BadRequestException


def raw_password_validator(senha):
    if len(senha) < 8:
        raise BadRequestException("Senha curta demais!")

    elif not any(c.isupper() for c in senha):
        raise BadRequestException("Deve conter ao menos uma letra Maiúscula!")

    elif not any(c.isloweer() for c in senha):
        raise BadRequestException("Deve conter ao menos uma letra Minúscula!")

    elif not any(c.isdigit() for c in senha):
        raise BadRequestException("Deve conter ao menos um Número!")
