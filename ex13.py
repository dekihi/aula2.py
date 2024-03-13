import os
os.system('cls')
import math 
print("Quantidade de ingressos necessarias para custear o espetaculo")

custo = float(input("Digite o investimento do teatro:"))
preço = float(input('Preço do convite: '))

quantidade = custo/preço

print(f'A quantidade de convites é: {quantidade:.0f}')
