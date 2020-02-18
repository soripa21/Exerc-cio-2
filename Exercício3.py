import random
quantidade_numeros =  float(input('Digite a quantidade de números: '))
lista = []
i=0

while i <= float(quantidade_numeros):
    lista.append(random.randrange(1,100))
    i = 1 + i

print('Essa é lista:', lista)
print('Esse é o maior valor da lista:', max(lista))
print('Esse é o maior valor da lista:', min(lista))