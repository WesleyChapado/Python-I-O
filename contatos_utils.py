#classe comum python para tratamento deste tipo de arquivo
import csv, pickle, json

#importa a classe Contato
from contato import Contato

def csv_para_contatos(caminho, encoding='latin_1'):
    contatos = []

    with open(caminho, encoding=encoding) as arquivo:
        #trata cada linha da leitura e remove as vírgulas
        leitor = csv.reader(arquivo)

        #lê linha por linha do arquivo e salva na lista "contatos"
        for linha in leitor:
            #desempacotamento, armazena cada item na sequencia que esta o arquivo
            id, nome, email = linha

            contato = Contato(id, nome, email)
            contatos.append(contato)

    return contatos

#salva o objeto em arquivo pickle
def contatoss_para_pickle(contatos, caminho):
    with open(caminho, mode='wb') as arquivo:
        pickle.dump(contatos, arquivo)

#le o arquivo com o objeto pickle
def pickle_para_contatos(caminho):
    with open(caminho, mode='rb') as arquivo:
        contatos = pickle.load(arquivo)

    return contatos

#salva o objeto em arquivo jason
def contatos_para_json(contatos, caminho):
    with open(caminho, mode='w') as arquivo:
        json.dump(contatos, arquivo, default=_contato_para_json)

#realiza a conversão dos objetos do tipo contato
def _contato_para_json(contato):
    return contato.__dict__

#lê os arquivos json
def json_para_contatos(caminho):
    contatos = []

    with open(caminho) as arquivo:
        contatos_json = json.load(arquivo)

        for contato in contatos_json:
            #desempacota cada linha por usar mesmo nome da variavel exemplo:
            #c = Contato(id=contato['id'], nome=contato['nome'], email=contato['email'])
            c = Contato(**contato)
            contatos.append(c)

    return contatos