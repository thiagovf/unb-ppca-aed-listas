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


def postFix(entrada):
    import re
    lista = re.split ("([^0-9])", entrada)
    pilha = Pilha()
    for token in lista:
        if token == '' or token == ' ' :
            continue
        if token == '+' :
            soma = pilha.desempilha() + pilha.desempilha()
            pilha.empilha(soma)
        elif token == '-' :
            subtracao = pilha.desempilha() - pilha.desempilha()
            pilha.empilha(subtracao)
        elif token == '*' :
            multiplicacao = pilha.desempilha() * pilha.desempilha()
            pilha.empilha(multiplicacao)
        elif token == '/' :
            divisao = pilha.desempilha() / pilha.desempilha()
            pilha.empilha(divisao)
        else:
            pilha.empilha(int(token))
    return pilha.desempilha() 

entrada = input()
print(postFix(entrada))