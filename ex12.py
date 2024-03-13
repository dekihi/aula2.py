import os
os.system("cls")
import math

print("Média Ponderada")
n1=float(input("Bota nota 1: "))
n2=float(input("Bota nota 2: "))
n3=float(input("Bota nota 3: "))

media_p = (2*n1+3*n2+5*n3)/10
print("\n")
print(("*")*40)
print(f"A sua média ponderada foi: {media_p}")
print(("*")*40)