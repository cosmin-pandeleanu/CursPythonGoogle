from math import gcd


class Fractie:
    def __init__(self, numarator, numitor):
        self.__numarator = numarator
        self.__numitor = numitor
        self.reduce()

    def __str__(self):
        return str(self.__numarator) + " / " + str(self.__numitor)

    def __add__(self, other):
        self.__numarator = self.__numarator * other.get_numitor() + other.get_numarator() * self.__numitor
        self.__numitor = self.__numitor * other.get_numitor()
        self.reduce()

    def __sub__(self, other):
        self.__numarator = self.__numarator * other.get_numitor() - other.get_numarator() * self.__numitor
        self.__numitor = self.__numitor * other.get_numitor()
        self.reduce()

    def inverse(self):
        self.__numarator, self.__numitor = self.__numitor, self.__numarator

    def get_numarator(self):
        return self.__numarator

    def get_numitor(self):
        return self.__numitor

    def reduce(self):
        d = gcd(self.__numarator, self.__numitor)
        self.__numarator = self.__numarator // d
        self.__numitor = self.__numitor // d


f = Fractie(10, 8)
g = Fractie(12, 9)
print("f = ", end="")
print(f)
print("g = ", end="")
print(g)

f.__add__(g)
print("f + g = ", end="")
print(f)

f = Fractie(10, 8)
f.__sub__(g)
print("f - g = ", end="")
print(f)

f = Fractie(10, 8)
f.inverse()
print("f ^-1 = ", end="")
print(f)
