palavra = str(input("Digite uma palavra para verificar se possui a letra A: "))

contagemA = palavra.count("A")
contagema = palavra.count("a")
total = contagemA + contagema
print("A palavra",palavra," contém",total," letras a.")

