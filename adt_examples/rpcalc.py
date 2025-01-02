from numbers import Number
from math import sin, cos


class RPCalc:
    def __init__(self):
        self.storage = []

    def push(self, n):
        if isinstance(n, Number):
            self.storage.append(n)
        elif n == "+":
            self.storage.append(self.pop()+self.pop())
        elif n == "-":
            self.storage.append(-self.pop()+self.pop())
        elif n == "*":
            self.storage.append(self.pop()*self.pop())
        elif n == "/":
            self.storage.append(1/self.pop()*self.pop())
        elif n == "sin":
            self.storage.append(sin(self.pop()))
        elif n == "cos":
            self.storage.append(cos(self.pop()))

    def pop(self):
        return self.storage.pop()

    def peek(self):
        return self.storage[-1]

    def __len__(self):
        return len(self.storage)
