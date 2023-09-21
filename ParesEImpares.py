"""
n = int(input())

pares = list()
impares = list()
for i in range(n):
    numero = int(input())
    if numero%2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)


pOrdenados = sorted(pares, reverse=False)
iOrdenados = sorted(impares, reverse= True)

for i in pOrdenados:
    print(i)

for i in iOrdenados:
    print(i)
"""
from estruturas.linkedList import LinkedList

lista = LinkedList()
print(lista._size)