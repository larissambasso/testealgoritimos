# 3) Descubra a lógica e complete o próximo elemento:
# a) 1, 3, 5, 7, ___
# b) 2, 4, 8, 16, 32, 64, ____
# c) 0, 1, 4, 9, 16, 25, 36, ____
# d) 4, 16, 36, 64, ____
# e) 1, 1, 2, 3, 5, 8, ____
# f) 2, 10, 12, 16, 17, 18, 19, ____

a = 9
b = 64*2
c = 7*7
d = 10*10
e = 5+8
f = 200


print("a) 1, 3, 5, 7,", a) #próximo impar
print("b) 2, 4, 8, 16, 32, 64,",b)#proximo dobro
print("c) 0, 1, 4, 9, 16, 25, 36,",c)#proximo quadrado da sequencia, no caso 7
print("d) 4, 16, 36, 64,",d)#sequência dos quadrados dos número naturais pares
print("e) 1, 1, 2, 3, 5, 8,",e)#proximo soma do anterior com o atual
print("f) 2, 10, 12, 16, 17, 18, 19,",f) #proximo tem que começar com a letra D