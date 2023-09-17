tempos = {
    'w': 1,
    'h': 1/2,
    'q': 1/4,
    'e': 1/8,
    's': 1/16,
    't': 1/32,
    'x': 1/64,
}
composicao = input().lower().replace('/', ' ').split()
while composicao[-1] != "*":
    contadorDeCompassos = 0
    for compassos in composicao:
        resultado = 0
        for identificador in compassos:
            resultado += tempos.get(identificador, 0)
        if resultado == 1:
            contadorDeCompassos += 1
    print(contadorDeCompassos)
    composicao = input().lower().replace('/', ' ').split()
print(type(tempos["x"]))
