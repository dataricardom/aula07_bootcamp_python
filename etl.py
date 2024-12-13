
#FUNÇÕES PARA LEITURA E ANALISE DE ARQUIVO CSV

import csv


path_arquivo = 'vendas.csv'

def leitura_csv(nome_arquivo_csv: str) -> list[dict]:
    
    lista=[]
    
    with open(nome_arquivo_csv, mode ='r', encoding='utf-8') as arquivo:
        leitor = csv.DictReader(arquivo)
        for linha in leitor:
            lista.append(linha)
    return lista


def filtrar_produtos_entregues(lista: list[dict]) -> list[dict]:
    lista_com_produtos_filtrados = []
    for produto in lista:
        if produto.get("entregue") == "True":
            lista_com_produtos_filtrados.append(produto)
    return lista_com_produtos_filtrados



def filtrar_tipo_produto(lista: list[dict]) -> list[dict]:
    lista_com_produtos_filtrados = []
    for produto in lista:
        if produto.get("produto") == "computador":
            lista_com_produtos_filtrados.append(produto)
    return lista_com_produtos_filtrados



def somar_valores_produtos(lista_com_produtos_filtrados: list[dict]) -> int:
    valor_total = 0
    for valor in lista_com_produtos_filtrados:
        valor_total += int(valor.get('price'))
            
    return valor_total


    