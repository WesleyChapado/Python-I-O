#abre o arquivo o '+' significa que foi aberto no modo de atualização
arquivo_contatos = open('dados/contatos-escrita.csv', encoding='latin_1', mode='a+')

#cria uma lista com os dados para inserção
contatos = ['11,Carol,carol@carol.com.br\n',
            '12,Ana,ana@ana.com.br\n',
            '13,Tais,tais@tais.com.br\n',
            '14,Felipe,felipe@felipe.com.br\n']

#escreve no arquivo cada item da lista
for contato in contatos:
    arquivo_contatos.write(contato)

#salva o arquivo
arquivo_contatos.flush()

#move o ponteiro para o caracter desejado
arquivo_contatos.seek(28)

#escreve no arquivo
arquivo_contatos.write('12,Ana,ana@ana.com.br\n'.upper())

arquivo_contatos.flush()
arquivo_contatos.seek(0)

#imprime o texto do arquivo
for linha in arquivo_contatos:
    print(linha)