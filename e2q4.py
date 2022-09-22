def fibo(qtdElementos):
    n1, n2 = 0, 1
    count = 0

    if qtdElementos != 1:
        while count < qtdElementos:
            nth: int = n1 + n2
            n1 = n2
            n2 = nth
            count += 1

    return n1

qtdElementos = int(input())
print(fibo(qtdElementos))