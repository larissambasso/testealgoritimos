# 4) Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:
# SP – R$67.836,43
# RJ – R$36.678,66
# MG – R$29.229,88
# ES – R$27.165,48
# Outros – R$19.849,53
# Escreva um programa na linguagem que desejar onde calcule o percentual
# de representação que cada estado teve dentro do valor total mensal da distribuidora.

sp = 67836.43
rj = 36678.66
mg = 29229.88
es = 27165.48
outros= 19849.53

distribuidora = sp + rj + mg + es + outros

percentualsp = 100*sp/distribuidora
percentualrj = 100*rj/distribuidora
percentualmg = 100*mg/distribuidora
percentuales = 100*es/distribuidora
percentualoutros = 100*outros/distribuidora

print(distribuidora)
print('O percentual do faturamento de sao paulo é de:{:.2f}%'.format(percentualsp))
print('O percentual do faturamento do Rio de Janeiro é de:{:.2f}%'.format(percentualrj))
print('O percentual do faturamento de Minas Gerais é de:{:.2f}%'.format(percentualmg))
print('O percentual do faturamento de Espirito Santo é de:{:.2f}%'.format(percentuales))
print('O percentual do faturamento de Outros estados é de:{:.2f}%'.format(percentualoutros))
