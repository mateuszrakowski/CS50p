class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        return "🍪" * self.size

    def deposit(self, n):
        if n + self.size > self.capacity:
            raise ValueError
        self.size = self.size + n
        return Jar(self.size)

    def withdraw(self, n):
        if n > self.size:
            raise ValueError
        self.size = self.size - n
        return Jar(self.size)

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        self._capacity = capacity
        if not isinstance(capacity, int) or capacity < 0:
            raise ValueError

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        self._size = size


def main():
    jar = Jar()


if __name__ == "__main__":
    main()