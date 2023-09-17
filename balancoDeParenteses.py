
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
