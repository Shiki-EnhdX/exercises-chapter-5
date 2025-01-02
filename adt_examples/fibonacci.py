class Fib:
    def __init__(self):
        self.value = (0, 1)

    def __iter__(self):
        return self

    def __next__(self):
        self.value = (self.value[1], self.value[0] + self.value[1])
        return self.value[1]
