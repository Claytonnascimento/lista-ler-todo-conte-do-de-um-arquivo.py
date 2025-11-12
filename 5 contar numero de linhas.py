with open("texto.txt", "r") as arquivo:
    linhas = 0
    for linha in arquivo:
        linhas += 1

print(f"O arquivo tem {linhas} linhas")
