import os 
os.system('cls')
import math

print('Calculadora de Peso')

peso = float(input('Digite o seu peso: '))

engorda = peso + peso * 15/100
emagrecer = peso - peso * 20/100

print(f'Seu peso caso engorde é: {engorda} KG.  Seu peso caso emagreça é: {emagrecer} KG')