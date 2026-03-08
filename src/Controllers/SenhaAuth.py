def SenhaAutenticador(senha):

    maiuscula = False
    minuscula = False
    numero = False

    validacao = False

    for c in senha:

        if c.isupper():
            maiuscula = True

        elif c.islower():
            minuscula = True

        elif c.isdigit():
            numero = True


    if maiuscula and minuscula and numero and len(senha) > 8:
        validacao = True

    else:
        print("Senha fraca ou não atende aos requisitos.\nRequisitos:\n-Letras Maiúsculas\n-Letras Minúsculas\n-Mais de 8 Caracteres")

    return validacao