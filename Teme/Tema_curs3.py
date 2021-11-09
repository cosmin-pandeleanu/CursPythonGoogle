def func1(*args, **kwargs):
    suma = 0
    for arg in args:
        if type(arg) == float or type(arg) == int:
            suma += arg
    return suma


def func2(n):
    if n == 0:
        return [0, 0, 0]
    elif n % 2 == 0:
        return [x + y for x, y in zip([n, n, 0], func2(n - 1))]
    else:
        return [x + y for x, y in zip([n, 0, n], func2(n - 1))]


def func3():
    try:
        n = int(input("Introdu o valoare => "))
        return n
    except ValueError:
        print("Valoare nu poate fi un numar intreg!")
        return 0


def main():
    print(func1(1, 5, -3, 'abc', [15, 56, 'cad']))
    print(func1())
    print(func1(2, 4, 'abc', pram_1=2))

    print(func2(5))

    print(func3())


main()
