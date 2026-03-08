def CPFAutenticador(CPF):

    letra = False
    numero = False
    outro = False
    validacao = False

    if len(CPF) == 11:
        validacao = True

    for c in CPF:

        if c.isdigit():
            numero = True

        elif c.isalpha():
            letra = True

        else:
            outro = True


    if letra or outro == True:
        validacao = False


    return validacao