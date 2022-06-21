# Dado a sequência de Fibonacci, onde se inicia por 0 e 1
# e o próximo valor sempre será a soma dos 2 valores anteriores 
# (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...),
# escreva um programa na linguagem que desejar onde,
# informado um número, ele calcule a sequência de Fibonacci e 
# retorne uma mensagem avisando se o número informado pertence ou não a sequência.

print("{}FIBONACCI{}".format('-'*20, '-'*20))
n = int(input('Digite quantos termos voce quer mostrar: '))
vetor = []
n1=0
n2=1
print("A sequencia de fibonacci começa assim: {} -> {}".format(n1, n2), end=' -> ')
f=3
while f <= n:
  soma = n1+n2
  print(soma, end=' -> ')
  n1 = n2
  n2 = soma
  f = f+1
vetor = soma
desejado = int(input("Digite um valor para ser encontrado ou nao na sequencia: "))
if desejado is vetor:
    print("Este numero esta na sequencia!")
else:
    print("Este numero nao esta na sequencia")
print('fim do programa')