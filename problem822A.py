"""
Como o problema trata a questao do MDC entre dois numeros, e, o fatorial é a sequencia
multiplicativa pelo antecessor até o 1, temos que o maximo divisor comum entre dois numeros fatoriais
sera o menor deles. Visto que o MDC de um numero é ele mesmo, e este, por sua vez, é parte da decomposição
multiplicativa do fatorial maior.
"""
def fatorial(n):
    if n == 0:
        return 1
    return n*fatorial(n-1)

entrada = input().split(" ")
menor = 0
if int(entrada[0]) > int(entrada[1]):
    menor = int(entrada[1])
elif int(entrada[0]) <= int(entrada[1]):
    menor = int(entrada[0])

print(fatorial(menor))