def calcular_troco(valores_moedas, troco, min_moedas, moedas_usadas):
    for centavos in range(troco + 1):
        cont_moedas = centavos
        nova_moeda = 1
        for j in [c for c in valores_moedas if c <= centavos]:
            if min_moedas[centavos - j] + 1 < cont_moedas:
                cont_moedas = min_moedas[centavos - j] + 1
                nova_moeda = j
        min_moedas[centavos] = cont_moedas
        moedas_usadas[centavos] = nova_moeda
    return min_moedas[troco]


def imprime_moedas(moedas_usadas, troco):
    moeda = troco
    while moeda > 0:
        this_moeda = moedas_usadas[moeda]
        print("%.2f" % round(this_moeda / 100, 2))
        moeda = moeda - this_moeda


def main():
    input() 
    moedas = input().split()
    nota_compra = input().split()

    moedas_int = []
    for moeda in moedas:
        moedas_int.append(int(round(float(moeda) * 100, 2)))

    troco = float(nota_compra[0]) - float(nota_compra[1])

    troco_int = int(round(troco * 100))

    moedas_usadas = [0] * 100
    cont_moedas = [0] * 100

    calcular_troco(moedas_int, troco_int, cont_moedas, moedas_usadas)
    imprime_moedas(moedas_usadas, troco_int)

main()