import os
from dataclasses import dataclass 
os.system("cls || clear")

@dataclass
class Livros:
    nome_do_livro : str
    autor : str
    categoria : str
    preco : float

lista_de_livros = []
quantidade_de_livros = 3

print(" == Informe os dados do livro == ")
for i in range(quantidade_de_livros):
        dados_do_livro = Livros(
        nome_do_livro = input("Digite o nome do livro : "),
        autor = input("Digite o nome do autor : "),
        categoria = input("Digite a categoria que esses livro pertence : "),
        preco = float(input("Digite quanto custa o livro : "))
        )