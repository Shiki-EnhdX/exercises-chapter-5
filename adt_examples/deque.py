class Deque:
    def __init__(self, size):
        self.size = size
        self.buffer = [None] * size
        self.start = 0
        self.end = 0
        self.length = 0

    def append(self, x):
        self.buffer[self.end] = x
        self.end = (self.end + 1) % self.size
        self.length += 1

    def appendleft(self, x):
        self.start = (self.start - 1) % self.size
        self.buffer[self.start] = x
        self.length += 1

    def pop(self):
        self.end = (self.end - 1) % self.size
        value = self.buffer[self.end]
        self.buffer[self.end] = None
        self.length -= 1
        return value

    def popleft(self):
        value = self.buffer[self.start]
        self.buffer[self.start] = None
        self.start = (self.start + 1) % self.size
        self.length -= 1
        return value

    def peek(self):
        return self.buffer[(self.end - 1) % self.size]

    def peekleft(self):
        return self.buffer[self.start]

    def __len__(self):
        return self.length

    def __iter__(self):
        return DequeIterator(self)


class DequeIterator:
    def __init__(self, deque):
        self.buffer = deque.buffer
        self.here = deque.start
        self.size = deque.size
        self.length = len(deque)

    def __iter__(self):
        return self

    def __next__(self):
        if self.length:
            value = self.buffer[self.here]
            self.here = (self.here + 1) % self.size
            self.length -= 1
            return value
        else:
            raise StopIteration
