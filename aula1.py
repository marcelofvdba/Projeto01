lista_inteiros = [12,34,56,100]

print(lista_inteiros)

lista_strings = ["Morango", "Uva","Banana"]

print(lista_strings)

lista_mista = ["Morango", 4.50, "Uva",9.00]

print(lista_mista)
#Posicao começa com 0
print(lista_mista[3])

#Tamanho de uma lista
print(len(lista_mista))

del lista_mista[:]
print(lista_mista)

#laços FOR

for i in lista_inteiros:
    print(i)

# Tupla sempre é definida por vírgula

tupla_numeros = 1,2,3,4
print(type(tupla_numeros))
print(tupla_numeros)

tupla_teste = 1
print(type(tupla_teste))

#tupla é usada quando os dados nunca serão mudados.

tupla_carros = "Gol", "Onix", "Fusca"
print(type(tupla_carros))
print(tupla_carros)

tupla_numeros1 = 2,3, 4, 5, 6

tupla_numeros = tupla_numeros + tupla_numeros1
print(tupla_numeros)

# iterar em uma tupla
if (2 in tupla_numeros):
    print("há numero")
else:
    print("Não há numeros")

#Coleção de dicionários

#Possuem uma chave e um valor e são escritos por {}

dicionario = {"chave": "Valor"}

estados_siglas = {"SC": "Santa Catarina", "PR": "Paraná"}
print(estados_siglas["PR"])

# Iterando com os dicionarios

for dic in estados_siglas:
    print(dic + " " + estados_siglas[dic])
#itens
for dic in estados_siglas.items():
    print(dic)
#chave
for dic in estados_siglas.keys():
    print(dic)
#valor
for dic in estados_siglas.values():
    print(dic)

#Adicionando Valor no Dicionario

estados_siglas["RJ"] = "Rio de Janeiro"
print(estados_siglas)

#Removendo Valor no Dicionario
del estados_siglas["PR"]
print(estados_siglas)

#EXE 1 LISTAS
lista_mista = [12,34,56,100, 150]
print(len(lista_mista))
#EXE 2 LISTAS
lista_string = ["ACDC", "RedHot"]
print (lista_string)
#adicionando valor na lista
lista_string.append("Metallica")
print (lista_string)

for i in lista_string:
    print(i)

del lista_string[2]
print (lista_string)
#EXE 3 TUPLAS
tupla_celulares1 = "Moto", "Apple"
print(tupla_celulares1)
print(type(tupla_celulares1))

#EXE 4 DICIONARIOS

paises_siglas = {"EUA": "Estados Unidos", "BRA": "Brasil"}
print(paises_siglas["EUA"])

# Iterando com os dicionarios
for dic in paises_siglas:
    print(dic + " " + paises_siglas[dic])

paises_siglas["ARG"] = "Argentina"
print(paises_siglas)
