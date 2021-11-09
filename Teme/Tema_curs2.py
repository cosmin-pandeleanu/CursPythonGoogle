lista = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]
print(lista)
lista_ = lista.copy()
lista_.sort()  # sortare cresc.
print(lista_)
lista_.sort(reverse=True)  # sortare desc.
print(lista_)

#functioneaza doar pentru lista data, ordonata crescator
lista_.sort()
print(lista_[1::2])  # numere pare
print(lista_[::2])   # numere impare
print(lista_[2::3])  # numere multipi de 3
#
print([i for i in lista if i % 2 == 0]) # numere pare
print([i for i in lista if i % 2 == 1]) # numere impare
print([i for i in lista if i % 3 == 0]) # numere multipi de 3
