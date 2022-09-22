class Pilha:
    def __init__(self):
        self.elementos = []
    
    def empilha(self, data):
        self.elementos.append(data)

    def desempilha(self):
        return self.elementos.pop()

    def tamanho(self):
        return len(self.elementos)

    def estaVazio(self):
        return self.tamanho == 0


def decimal2binario(numero):
    pilha = Pilha()
    pilha.__init__()
    while (numero >= 2):
        resto = numero%2
        pilha.empilha(str(resto))
        aux = int(numero/2)
        numero = aux
    pilha.empilha(str(numero))

    if pilha.estaVazio():
        return ''

    strbin = ''
    for i in range(pilha.tamanho()):
        strbin += pilha.desempilha()
    
    return strbin
