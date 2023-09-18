
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


def rearrange_trains(A, B):
    station = Stack()
    output_sequence = []

    while B:
        if not station.isEmpty() and station.peek() == B[0]:
            output_sequence.append("R")
            station.pop()
            B.pop(0)
        else:
            if A:
                output_sequence.append("I")
                station.push(A.pop(0))
            else:
                return "".join(output_sequence)+" Impossible"
    return "".join(output_sequence)


while True:
    N = int(input())

    if N == 0:
        break

    A = list(input().split())
    B = list(input().split())

    result = rearrange_trains(A, B)
    print(result)
