#lista com a denominação numero e a varivel com a denominação par 
numeros = []
par=0
#o renge ira repitir uma ação 5 vezes 
for i in range(0,5):
#pede para o usuario colocar os numeros 
    numero = int(input(f'Digite o {i+1}° número: '))
#Se o número for par adicionar 1 a variável "par"
    if numero % 2 == 0:
        par = par+1
#Mostra quantos números pares existem na lista
print(f"{par} valores pares")