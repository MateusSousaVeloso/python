user = input("Digite o nome do usuário: ")
if user == "Arthur":
    senha = int(input("Digite a senha do usuário: "))
    if senha == 12345:
        print("Acesso permitido")
    else:
        print("Senha incorreta")
else:
    print("Usuário não encontrado")

user_n = input("Digite o nome do segundo usuário: ")
match user_n:
    case "Admin":
        senha_n = int(input("Digite a senha do segundo usuário: "))
        match senha_n:
            case 98765:
                print("Acesso permitido")
            case _:
                print("Senha incorreta")
    case _:
        print("Usuário não encontrado")