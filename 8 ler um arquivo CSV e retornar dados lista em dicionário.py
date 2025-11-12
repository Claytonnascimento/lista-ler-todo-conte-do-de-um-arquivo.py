import csv

print("\nLer arquivo CSV (exemplo.csv)")
with open('exemplo.csv', 'r') as csvfile:
    leitor = csv.DictReader(csvfile)
    dados = list(leitor)
    for linha in dados:
        print(linha)
