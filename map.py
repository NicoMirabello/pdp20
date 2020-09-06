def doblar (numero):
    return numero*2

numeros = [2,3,4,5,6]

map(doblar,numeros)

print (list(map(doblar,numeros)))
