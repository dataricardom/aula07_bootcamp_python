from etl import leitura_csv,filtrar_tipo_produto,filtrar_produtos_entregues,somar_valores_produtos
path_arquivo = 'vendas.csv'
lista_de_produtos = leitura_csv(path_arquivo)
produtos_entregues = filtrar_produtos_entregues(lista_de_produtos)
soma_produtos = somar_valores_produtos(produtos_entregues)
produtor_tipo = filtrar_tipo_produto(lista_de_produtos)

print(produtor_tipo)