f = open('seu-arquivo.txt', 'r')
familia = f.readlines()
familia.append('Max;7')
f = open('seu-arquivo.txt', 'w')
f.writelines(familia)
f.close()

print(f.readlines())
