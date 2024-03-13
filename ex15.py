import os
os.system ('cls')
import math

print('o pobre João')

Salario = float(input('O salario de João é:'))

conta1 = float(input('Valor da conta 1:'))
conta2 = float(input("Valor da conta 2: "))

conta_total1 = conta1 + conta1 * 2/100
conta_total2 = conta2 + conta2 * 2/100
sobra_salario = Salario - (conta_total1+conta_total2)

print(f'O salario sobrado será:{sobra_salario}')