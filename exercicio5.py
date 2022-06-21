# 5) Escreva um programa que inverta os caracteres de um string.

# IMPORTANTE:
# a) Essa string pode ser informada através de qualquer entrada 
# de sua preferência ou pode ser previamente definida no código;

# b) Evite usar funções prontas, como, por exemplo, reverse;

A = str(input("insira o valor de A:"))
B = str(input("insira o valor de B:"))
print(A,B)
C = A
A = B
B = C
print("Ao fazermos a inversão, A vale: {} e B vale {}".format(A,B))