origem = open('texto.txt', 'r')
destino = open('copia.txt', 'w')
conteudo = origem.read()
destino.write(conteudo)
origem.close()
destino.close()

print("\nArquivo copiado para 'copia.txt'")
