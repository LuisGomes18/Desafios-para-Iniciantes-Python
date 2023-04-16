from os import system


bot_1 = {
    "prefixo_bot_1": "",
    "nome_bot_1": "",
    "linguagem_programacao_bot_1": "",
    "convite_bot_1": ""
}

bot_2 = {
    "prefixo_bot_2": "",
    "nome_bot_2": "",
    "linguagem_programacao_bot_2": "",
    "convite_bot_2": ""
}

bot_3 = {
    "prefixo_bot_3": "",
    "nome_bot_3": "",
    "linguagem_programacao_bot_3": "",
    "convite_bot_3": ""
}

comandos = ["?ajuda", "?exit", "?ping", "?addbot", "?ban", "?denunciar", "?kick", "?medalha", "?npm", "?reclamacao", "?recomendacao", "?requisitos", "?solicitar tag", "?sugestao", "timeout"]
linguagens_programacao_aceites = ["python", "javasricpt", "java", "lua", "typescript"]
medalhas_aceites = ["Fundador", "Desenvolvedor Equipa", "Punidor", "Mensageiro", "Sujestor", "1 ano na Comunidade", "2 anos na Comunidade"]
senha_real = '$+ud(UE+D]TZ]2&JVWbyONlVk'
prefixo = '?'
vezes_add_bot = 1
system("clear")
print('Código pronto\n')

while True:
    chat = input('\nComando: ')
    x = chat.find(prefixo)
    if chat == '?ajuda' and x == 0:
        print('\033[1m' + 'Ajuda\n' + '\033[0;0m')
        print('exit - Para parar o código\nping - Para saber a latencia do código\naddbot - Adicionar bot ao "server"\nban - Para banir alguem do "server" [so staff]\ndenunciar - Para denunciar alguem\nkick - Para kickar alguem do server [so staff]\nmedalha - Para dar uma medalha a alguem [so staff]\nnpm - Pesquisar sobre um package de javasricpt\nreclamacao - Para reclamar de um serviço de alguem\nrecomendacao - Recomendar algum serviço de alguem\nrequisitos - Para saber sobre os requisitos de tag\nsolicitar tag - Para pedir a staff alguma tag\nsugestao - Para sugerir algo novo para o server\ntimeout - Não sei mudar')

    elif chat == '?ping' and x == 0:
        print('Eu sou um robo?? EU SOU UM ROBO?? EU SOU UM RO...? Eu sou um mostro afastem se de mim')

    elif chat == '?addbot' and x == 0:
        if vezes_add_bot == 1:
            bot_1["prefixo_bot_1"] = input('Qual prefixo do bot: ')
            bot_1["nome_bot_1"] = input('Qual o nome do bot: ')
            bot_1["linguagem_programacao_bot_1"] = input('Qual linguagem de programacao do bot: ')
            bot_1["convite_bot_1"] = input('Qual convite do bot: ')
            prefixo_bot_1 = bot_1["prefixo_bot_1"]
            nome_bot_1 = bot_1["nome_bot_1"]
            linguagem_programacao_bot_1 = bot_1["linguagem_programacao_bot_1"]
            while linguagem_programacao_bot_1 not in linguagens_programacao_aceites:
                bot_1["linguagem_programacao_bot_1"] = input('Qual linguagem de programacao do bot: ')
            convite_bot_1 = bot_1["convite_bot_1"]
            print('\033[1m' + '\nBOT 1' + '\033[0m' + f'\nPrefixo : {prefixo_bot_1}\nNome do bot : {nome_bot_1}\nLinguagem de programacao: {linguagem_programacao_bot_1}\nConvite do bot : {convite_bot_1 }')
            print('\033[32m' + '\nBot adicionado' + '\033[0m')
            vezes_add_bot += 1

        elif vezes_add_bot == 2:
            bot_2["prefixo_bot_2"] = input('Qual prefixo do bot: ')
            bot_2["nome_bot_2"] = input('Qual o nome do bot: ')
            bot_2["linguagem_programacao_bot_2"] = input('Qual linguagem de programacao do bot: ')
            bot_2["convite_bot_2"] = input('Qual convite do bot: ')
            prefixo_bot_2 = bot_2["prefixo_bot_2"]
            nome_bot_2 = bot_2["nome_bot_2"]
            linguagem_programacao_bot_2 = bot_2["linguagem_programacao_bot_2"]
            while linguagem_programacao_bot_2 not in linguagens_programacao_aceites:
                bot_2["linguagem_programacao_bot_2"] = input('Qual linguagem de programacao do bot: ')
            convite_bot_2 = bot_2["convite_bot_2"]
            print('\033[1m' + '\nBOT 2' + '\033[0m' + f'\nPrefixo : {prefixo_bot_2}\nNome do bot : {nome_bot_2}\nLinguagem de programacao: {linguagem_programacao_bot_2}\nConvite do bot : {convite_bot_2 }')
            print('\033[32m' + '\nBot adicionado' + '\033[0m')
            vezes_add_bot += 1

        elif vezes_add_bot == 3:
            bot_3["prefixo_bot_3"] = input('Qual prefixo do bot: ')
            bot_3["nome_bot_3"] = input('Qual o nome do bot: ')
            bot_3["linguagem_programacao_bot_3"] = input('Qual linguagem de programacao do bot: ')
            while linguagem_programacao_bot_3 not in linguagens_programacao_aceites:
                bot_3["linguagem_programacao_bot_3"] = input('Qual linguagem de programacao do bot: ')
            bot_3["convite_bot_3"] = input('Qual convite do bot: ')
            prefixo_bot_3 = bot_3["prefixo_bot_3"]
            nome_bot_3 = bot_3["nome_bot_3"]
            linguagem_programacao_bot_3 = bot_3["linguagem_programacao_bot_3"]
            convite_bot_3 = bot_3["convite_bot_3"]
            print('\033[1m' + '\nBOT 3' + '\033[0m' + f'\nPrefixo : {prefixo_bot_3}\nNome do bot : {nome_bot_3}\nLinguagem de programacao: {linguagem_programacao_bot_3}\nConvite do bot : {convite_bot_3 }')
            print('\033[32m' + '\nBot adicionado' + '\033[0m')
            vezes_add_bot += 1

        elif vezes_add_bot >= 4:
            print('Já adicionou muitos bots')

    elif chat == '?ban' and x == 0:
        nome_usuario_ban = input('Insira o nome de usuario: ')
        motivo_ban = input('Insira o motivo do ban: ')
        senha = input('Insira a senha para dar ban: ')
        while senha != senha_real:
            senha = input('Insira a senha para dar ban: ')
        print('\033[1m' + 'BAN' + '\033[0m' + f'Nome do usuario: {nome_usuario_ban}\nMotivo: {motivo_ban}')
        print('\033[32m' + '\nBanimento feito' + '\033[0m')

    elif chat == '?denunciar' and x == 0:
        nome_usuario_denuncia = input('Insira o nome de usuario: ')
        motivo_denuncia = input('Insira o motivo da denuncia: ')
        prova = input('Insira a prova: ')
        print('\033[1m' + 'DENUNCIA' + '\033[0m' + f'Nome do usuario: {nome_usuario_denuncia}\nMotivo: {motivo_denuncia}\nProva: {prova}')
        print('\033[32m' + '\nDenuncia feita' + '\033[0m')

    elif chat == '?kick' and x == 0:
        nome_usuario_kick = input('Insira o nome de usuario: ')
        motivo_kick = input('Insira o motivo do kick: ')
        senha = input('Insira a senha para dar kick: ')
        while senha != senha_real:
            senha = input('Insira a senha para dar kick: ')
        print('\033[1m' + 'KICK' + '\033[0m' + f'Nome do usuario: {nome_usuario_kick}\nMotivo: {motivo_kick}')
        print('\033[32m' + '\nKick feito' + '\033[0m')

    elif chat == '?medalha' and x == 0:
        nome_usuario_medalha = input('Insira o nome de usuario: ')
        medalha = input('Insira qual medalha quer dar: \n->Fundador\n->Desenvolvedor Equipa\n->Punidor\n->Mensageiro\n->Sujestor\n->1 ano na Comunidade\n->2 anos na Comunidade\n--> ')
        while medalha not in medalhas_aceites:
            medalha = input('Insira qual medalha quer dar: \n->Fundador\n->Desenvolvedor Equipa\n->Punidor\n->Mensageiro\nSujestor\n->1 ano na Comunidade\n->2 anos na Comunidade\n--> ')
        mensagem = input('Insira a mensagem ao ganhador da medalha: ')
        print('\033[1m' + 'MEDALHAS' + '\033[0m' + f'Nome do usuario: {nome_usuario_medalha}\nMedalha: {medalha}')
        print('\033[32m' + '\nMedalha atribuida' + '\033[0m')

    elif chat == '?npm' and x == 0:
        print('Em construção')

    elif chat == '?reclamacao' and x == 0:
        nome_usuario_reclamacao = input('Insira o nome do usuario: ')
        serviço_reclamacao = input('Insira qual foi o serviço: ')
        motivo_reclamacao = input('Insira qual o motivo: ')
        print('\033[1m' + 'RECLAMAÇÃO' + '\033[0m' + f'Nome do usuario: {nome_usuario_kick}\nMotivo: {motivo_kick}')
        print('\033[32m' + '\nReclamacao enviada' + '\033[0m')

    elif chat == '?recomendacao' and x == 0:
        nome_usuario_recomendacao = input('Insira o nome do usuario: ')
        serviço_recomendacao = input('Insira qual foi o serviço: ')
        nota_recomendacao = input('Insira a nota que da ao serviço: ')
        print('\033[32m' + '\nRecomendacao enviada' + '\033[0m')

    elif chat == '?requisitos' and x == 0:
        print('''Requisitos para ser Desenvolvedor
    - Conhecer a linguagem totalmente
    - Ter repositório no GitHub com a linguagem trabalhada;
    - Não pode ocorrer nenhum erro no código;
    - Não pode ser compartilhado para lojas ou uso em servidores;

Dono de Hospedagem
    - Ter 500 membros no Discord;
    - Ter 60 membros on-line por 7 dias;
    - Ter planos com mais de 8GB;
    - Ter mais de 10 clientes usando a host;
    - Seguir todas as ToS e Guildelines do Discord;

Dono de Servidor
    - Ter 300 membros no Discord;
    - Ter 30 membros on-line por 7 dias;
    - Ter 10 vips ativos no servidor e no Discord;
    - Seguir todas as ToS e Guildelines do Discord;

Dono de Loja
    - Ter 200 membros no Discord;
    - Ter 15 membros on-line por 7 dias;
    - Ter mais de 10 avaliaçõse pelos clientes;
    - Ter mais de 10 clientes ativos;
    - Seguir todas as ToS e Guildelines do Discord;

Requisitos para Parceiro
    - Ter 100 membros no Discord;
    - Seguir todas as ToS do Discord;
    - Não conter NSFW/NSFL;
    - Todos os membros seguir as regras normalmente do servidor;
    - Staff/Servidor organizado.

Requisitos para Afiliado
    - Ter 50 membros no Discord;
    - Seguir todas as ToS do Discord;
    - Não conter NSFW/NSFL;
    - Todos os membros seguir as regras normalmente do servidor;
    - Staff/Servidor organizado.

GPA (Guildelines Partners and Affiliates)
    1° - Servidor é obrigado a ter o cargo Parceiros para fazer parceria com a comunidade;
    2° - Quaisquer grupo tem que mencionar here com o texto que será enviado para o representante;
    3° - PROIBIDO LOJAS que vendam derrubar contas de redes sociais, produtos relacionados ao Discord, bots para apostas e malwares;
    4° - Não aceitamos renovação de parceria por menos de 15 dias;
    5° - Se o parceiro e dono de um servidor de minecraft, hospedagem, loja de plugins, etc. Recebem tag extra;
    6° - Não aceitamos parcerias replicas com o nosso Discord;
    7° - Para fazer parceria e necessário usar o comando /solicitar parceria, se caso o comando não estiver funcionando contate com o Dono ou a Equipe de Parcerias;
''')

    elif chat == '?solicitar' and x == 0:
        tag = input('->Tag\n->Parceria\n-->')
        if tag == 'Tag':
            print('Em contrução')
        elif tag == 'Parceria':
            link_parceria = input('Insira o link do servidor: ')
            texto_parceria = input('Insira o texto: ')
            print('\033[32m' + '\nPedido para parceria feita' + '\033[0m')
    
    elif chat == '?sugestao' and x == 0:
        print('Insira sua sugestao: ')
        print('\033[32m' + 'Sugestão enviada' + '\033[0m')

    elif chat == 'timeout' and x == 0:
        nome_usuario_timeout = input('Insira o nome de usuario: ')
        motivo_timeout = input('Insira o motivo: ')
        tempo_timeout = input('Insira o tempo: ')
        senha = input('Insira a senha: ')
        if senha == senha_real:
            print('\033[32m' + 'Timeout feito' + '\033[0m')
        elif senha != senha_real:
            print('Senha errada')


    elif chat == '?exit' and x == 0:
        print('Adeus')
        exit()

    elif chat not in comandos:
        print('Comando não encontrado')

    elif x == -1 or x >= 2:
        print('Prefixo errado')
