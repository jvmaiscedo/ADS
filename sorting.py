def quickSort(lista, inicio=0, fim=None):
    if fim is None:
        fim = len(lista)-1
    if inicio < fim:
        p = partition(lista, inicio, fim)
        quickSort(lista, inicio, p-1)
        quickSort(lista, p+1, fim)
    return lista

def partition(lista, inicio, fim):
    pivot = lista[fim]
    i = inicio
    for j in range(inicio, fim):
        if lista[j] < pivot:
            lista[j], lista[i] = lista[i], lista[j]
            i = i+1

    lista[i], lista[fim] = lista[fim], lista[i]
    return i


def mergeSort(lista, inicio=0, fim=None):
    if fim == None:
        fim = len(lista)
    if (fim-inicio) > 1:
        meio = (fim+inicio)//2
        mergeSort(lista, inicio, meio)
        mergeSort(lista, meio, fim)
        merge(lista, inicio, meio, fim)

    return lista

def merge(lista, inicio, meio, fim):
    left = lista[inicio:meio]
    right = lista[meio:fim]
    top_left, top_right = 0, 0
    for k in range(inicio, fim):
        if top_left >= len(left):
            lista[k] = right[top_right]
            top_right += 1
        elif top_right >= len(right):
            lista[k] = left[top_left]
            top_left += 1
        elif left[top_left] < right[top_right]:
            lista[k] = left[top_left]
            top_left += 1
        else:
            lista[k] = right[top_right]
            top_right += 1





already_sorted = [1, 2, 3, 4, 5, 6, 9, 20, 22, 23, 28,
                    32, 34, 39, 40, 42, 76, 87, 99, 112]

inversed = [117, 90, 88, 83, 81, 77, 74, 69, 64, 63, 51,
            50, 49, 42, 41, 34, 32, 29, 28, 22, 16, 8, 6, 5, 3, 1]

repeated = [7, 7, 7, 7, 7, 1, 1, 9, 9, 0, 4, 4, 4, 5, 4, 5, 7, 1,]

print(mergeSort(repeated))
