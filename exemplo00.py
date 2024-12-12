from typing import List

#Função para calcular media de valores em uma lista
valores1 = [5.0,5.0,5.0]

def calcular_media(valores: List[float]) -> float:
    return sum(valores) / len(valores)


valores = calcular_media(valores1)

print(valores)

#Função para filtrar dados acima do limite

lista_de_valores = [50,30,40,100,10,15]
limite = 40


def filtrar_dados_acima(valores: List[float], limite: float) -> List[float]:
    resultado = []
    for valor in valores:
        if valor > limite:
            resultado.append(valor)
    return resultado

resultado = filtrar_dados_acima(lista_de_valores, limite)

print(resultado)



def contar_valores_unicos(lista: List[int]) -> int:
    return len(set(lista))


lista_valores = contar_valores_unicos(lista_de_valores)

print(lista_valores)

#Função para converter Celcius para Fahrenheint em uma lista
temperaturas =[ 35.0,33.66,20.0]

def celcius_para_fahrenheit(temperaturas_celcius: List[float] ) -> List[float]:
    return [(9/5) * temp + 32 for temp in temperaturas_celcius]

conversao_temperaturas = celcius_para_fahrenheit(temperaturas)

print(conversao_temperaturas)

# Recebendo nome e dando boas vindas
vulgo = 'Ricardo Marques'
def boas_vindas(nome: str) -> str:
    return 'Bem vindo ' + nome  

boas_vindas_2 = boas_vindas(vulgo)

print(boas_vindas_2)


#Função para calculo de desvio padrão
lista_valores = [10.0,5.5,7.8,9.0]


def calc_desvio(valores: List[float]) -> float:
    media = sum(valores) / len(valores)
    variancia = sum((x - media) ** 2 for x in valores) / len(valores)
    return variancia ** 0.5

desvio = calc_desvio(lista_de_valores)

print(desvio)

#Função encontrar valores ausentesem uma sequencia

numeroslista= [10,55,78,90]
def encontrar_valores_ausentes(sequencia: List[int]) -> List[int]:
    completo = set(range(min(sequencia), max(sequencia)+1))

    return list(completo - set(sequencia))

ausentes = encontrar_valores_ausentes(numeroslista)

print(ausentes)