"""
Entrada: Dois trechos de código genético, uma em cada linha.
Saída: A mais longa sequência comum entre os trechos de código.
Por exemplo, dada as sequências: 
CAGGGTAGTC
TCATATC
a mais longa sequência comum é CATATC.
LCS - Longest Common Subsequence.
Algoritmo recursivo: The Naive Solution
"""

def LCS(X, Y, m, n):
    menosM = m - 1;
    menosN = n - 1;
    if m == 0 or n == 0:
        return(0);
    elif X[menosM] == Y[menosN]:

        return 1 + LCS(X, Y, menosM, menosN);
    else: 
        return max(LCS(X, Y, m, menosN), LCS(X, Y, menosM, n));

s1 = input()
s2 = input()

tamanho = LCS(s1,s2, len(s1), len(s2));
print(tamanho) 