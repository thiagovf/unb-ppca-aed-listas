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
        else:
            topo = pilha.elementos[-1]
            if (caracter == ")" and topo == "(") or (caracter == "]" and topo == "[") or (caracter == "}" and topo == "{"):
                pilha.pop()
            else:
                return False
        
    return pilha.tamanho() == 0

x = input()
print(verificaParanteses(x))