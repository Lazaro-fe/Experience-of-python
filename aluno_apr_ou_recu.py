import os
os.system("cls || clear")

nome = input("Digite seu nome: ")
teste = float(input("Digite a sua nota do teste: "))
prova = float(input("Digite a sua nota da prova: "))
qualitativo = float(input("Digite a nota do qualitativo: "))
media = (teste + prova + qualitativo) / 3

os.system("cls || clear")

if media >= 6:
    print()
    print("===== Esse aluno foi aprovado com sucesso!! =====")
else:
    print()
    print("===== Esse aluno se encontra na recuperação!! =====")


print()
print(f"A nota do teste de {nome} foi : {teste}")
print(f"A nota da prova de {nome} foi : {prova}")
print(f"A nota do qualitativo de {nome} foi : {qualitativo}")
print(f"A média de {nome} foi de : {media:.2f}")