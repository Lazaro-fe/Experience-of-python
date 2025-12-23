import os
os.system("cls || clear")

preco = float(input("Qual o preço do produto? US$"))
imposto = (preco * 60) / 100

print()
print(f"Preco: US$ {preco}")
print(f"Imposto à ser pago: US$ {imposto}")