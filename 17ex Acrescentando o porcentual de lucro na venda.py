'''  Faça um programa que leia dois números, o preço de custo de um produto e seu percentual 
de lucro. Calcule e retorne seu preço de venda: '''


valor = float(input('Valor do produto: '))
percentual = float(input('Percentual de lucro: '))
decimal = percentual*0.01
valor_final = valor + (valor*decimal)
print(f'O preço da venda desse produto é {valor_final}')
