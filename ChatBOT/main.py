from json import loads

comandos = ['?exit', '?ajuda', '?help', '?ban', '?changelog adicionar', '?changelog remover']
prefixo = '?'
senha = 'wjEMYx%AMJWX.-t6dkV$E},f1_@,LPfn9'
cargos = ['membro', 'moderador', 'admistrador', 'dono']
membro = {"nome": "",
          "cargos": ["membro"],
          }

dados_membro = loads(str(membro))

# print(y["age"])

while True:
    comando_usuario = str(input('Insira o comando: '))
    comando_usuario.lower()
    x = comando_usuario.find(prefixo)

    if comando_usuario == '?exit' and x == 0 and comando_usuario in comandos:
        print('Tchau :(')
        break

    elif comando_usuario == '?ajuda' or comando_usuario == '?help' and x == 0 and comando_usuario in comandos:
        print('''?exit - Para sair do codigo
?help, ?ajuda - Para ver os comandos
        ''')

    elif comando_usuario == '?ban' and x == 0 and comando_usuario in comandos:
        nome_usuario = str(input('Insira o nome do mebro (exemplo: LuisGomes#6625): '))
        movito_ban = str(input('Insira o movito do banimentos: '))
        senha_banir = str(input('Insira a senha: '))
        if senha_banir == senha:
            print('Membro banido com sucesso')
        elif senha_banir != senha:
            print('Senha incorreta')

    elif comando_usuario == '?changelog adicionar' and x == 0 and comando_usuario in comandos:
        nome_usuario = str(input('Insira o nome do membro (exemplo: LuisGomes#6625): '))
        cargo = str(input('Insira o cargo: '))
        if cargo in cargos:
            print('Membro adicionado')

    elif comando_usuario == '?changelog remover' and x == 0 and comando_usuario in comandos:
        nome_usuario = str(input('Insira o nome do membro (exemplo: LuisGomes#6625): '))
        cargo = str(input('Insira o cargo que e para remover: '))
