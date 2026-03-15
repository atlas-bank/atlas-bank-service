def SenhaAutenticador(senha):
    if len(senha) < 8:
        raise Exception("Senha curta demais!")

    elif not any(c.isupper() for c in senha):
        raise Exception("Deve conter ao menos uma letra Maiúscula!")

    elif not any(c.isloweer() for c in senha):
        raise Exception("Deve conter ao menos uma letra Minúscula!")

    elif not any(c.isdigit() for c in senha):
        raise Exception("Deve conter ao menos um Número!")