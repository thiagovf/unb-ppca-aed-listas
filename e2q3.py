class Pilha:
    def __init__(self):
        self.elementos = []
    
    def push(self, data):
        self.elementos.append(data)

    def pop(self):
        return self.elementos.pop()

    def tamanho(self):
        return len(self.elementos)

    def estaVazio(self):
        return self.tamanho == 0

def verificaParanteses(entrada):
    pilha = Pilha()
    
    for caracter in entrada:
        if caracter == '(' or caracter == '[' or caracter == '{':
            pilha.push(caracter)
        elif caracter == ')' or caracter == ']' or caracter == '}':
            if pilha.tamanho() > 0:
                pilha.pop()
            else:
                pilha.push(caracter)
                break
        
    return pilha.tamanho() == 0

x = input()
print(verificaParanteses(x))
