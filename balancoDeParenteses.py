"""
Dada uma expressão qualquer com parênteses, indique se a quantidade de parênteses está correta ou não, sem levar em
conta o restante da expressão. Por exemplo:

a+(b*c)-2-a        está correto
(a+b*(2-c)-2+a)*2  está correto

enquanto

(a*b-(2+c)         está incorreto
2*(3-a))           está incorreto
)3+b*(2-c)(        está incorreto

Ou seja, todo parênteses que fecha deve ter um outro parênteses que abre correspondente e não pode haver parênteses que
fecha sem um previo parenteses que abre e a quantidade total de parenteses que abre e fecha deve ser igual.

Entrada
Como entrada, haverá N expressões (1 <= N <= 10000), cada uma delas com até 1000 caracteres.

Saída
O arquivo de saída deverá ter a quantidade de linhas correspondente ao arquivo de entrada, cada uma delas contendo as
palavras correct ou incorrect de acordo com as regras acima fornecidas.
"""


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
        else:
            raise IndexError("A pilha está vazia.")

    def peek(self):
        if not self.isEmpty():
            return self.items[-1]
        else:
            raise IndexError("A pilha está vazia.")

    def isEmpty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


def balanco_de_parenteses(expression):

    parentesesDireito = Stack()

    for itens in expression:
        if itens == "(":
            parentesesDireito.push(itens)
        elif itens == ")" and parentesesDireito.isEmpty():
            return "incorrect"
        elif itens == ")" and not parentesesDireito.isEmpty():
            parentesesDireito.pop()

    if parentesesDireito.isEmpty():
        return "correct"
    else:
        return "incorrect"


while True:
    try:
        expressao = input()
        print(balanco_de_parenteses(expressao))
    except EOFError:
        break
