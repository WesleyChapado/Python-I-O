import contatos_utils

try:
    #executa as funções que criamos em contato_utils
    #contatos = contatos_utils.csv_para_contatos('dados/contatos.csv')
    #contatos_utils.contatoss_para_pickle(contatos, 'dados/contatos.pickle')
    #contatos = contatos_utils.csv_para_contatos('dados/contatos.pickle')

    #imprime linha por linha
    for contato in contatos:
        print(f'{contato.id} - {contato.nome} - {contato.email}')

#exemplo de tratamento de arquivo
except FileNotFoundError:
    print('Arquivo não encontrado')

except PermissionError:
    print('Sem Permissão de escrita')
