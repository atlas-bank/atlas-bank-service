from View.LoginView import menu
from View.LoginView import logincpf
from View.LoginView import loginsenha
from View.LoginView import saida
from Controllers.SenhaAuth import raw_password_validator
from Controllers.CPFAuth import CPFAutenticador

while True:

    opcao = menu()

    if opcao == "1":
        cpf = logincpf()

        validacaoCPF = CPFAutenticador(cpf)

        if validacaoCPF:
            senha = loginsenha()
            validacaoSenha = raw_password_validator(senha)

            if validacaoSenha:
                print("\nVocê fez Login!")
                break

            else:
                print("\nNão fez login!")

        elif validacaoCPF == False:
            print("CPF Inválido!")

    elif opcao == "0":
        saida()
        break

    else:
        print("\nOpção Inválida, tente novamente...")