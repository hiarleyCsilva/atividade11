km2 = 0.45
km1 = 0.50
distancia = float(input("Qual a distância da sua viagem em km?: "))

if distancia < 200:
    preco = km1 * distancia
else:
    preco = km2 * distancia

print("O preço da sua viagem é: R$ {:.2f}".format(preco))

