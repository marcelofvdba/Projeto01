
#Funções com argumentos inteiros

def soma(x,y):
    return x + y


print(soma(2,2))

s = soma(2,2)

print(s)


#Funções com argumentos strings

def identificacao(meu_nome, idade):
    print (f"Olá {meu_nome} Sua idade é {idade}")

identificacao("João", 34)

#Funções com argumentos ou Parametros Nomeados

identificacao(idade=34,meu_nome="Joao")

#Funções com argumentos chumbado

def identificacao(meu_nome, idade=60):
    print (f"Olá {meu_nome} Sua idade é {idade}")

identificacao("João")

## Funções com condicionais
##salario + imposto
salario = float(input("Digite o Salario: "))

def salario_desconta_imposto(salario, imposto=27.0):
    print(salario - (salario * imposto * 0.01))

salario_desconta_imposto(salario, imposto=10.0)

def validausuario(nome_usuario,senha):
    if nome_usuario == "admin" and senha == "Floripa":
        return("Usuário e senha correto. Bem Vindo")
    elif nome_usuario == "admin":
        return("Usuário está Correto")
    elif senha == "floripa":
        return("Senha Correta")
    else:
        print("Usuário e senha Incorretos")

print(validausuario("admin","Floripa"))


#Chamando outra função dentro dela.

def calculo(num1,num2, funcao=soma):
    return soma(num1,num2)

print(calculo(2,2))

def subtracao(num1,num2):
    return num1 - num2

print(calculo(2,2,subtracao))

#*args é para usar quando não sabe quantos parametros e retornam em tuplas
#*kwargs é para argumentos nomeados e retornam dicionarios

#def soma(*args):
 #print(args)
    #soma(2,3,3,4,4,55)

def soma_total(*args):
    total = 0
    for numero in args:
        total = numero + total
        return total
print(soma_total(25,27,29,26,28))

#################kwargs

def saudacoes(**kwargs):
    print(kwargs)

saudacoes(manha="bom dia", tarde="Boa Tarde",noite="Boa Noite")

def saudacoes_dia(**kwargs):
    for hora, saudacao in kwargs.items():
        print(f"Durante a {hora} dizemos {saudacao} ")

saudacoes_dia(manha = "Bom dia", tarde="Boa tarde", noite="Boa noite")


####Funções decoradoras####

def master(msg):
    def imprime():
        print("Essa é função principal. ")
        msg() #precisa dizer que este é um argumento vazio
    return imprime


def chama_funcao():
    print("Essa é a Segunda Função. ")

chama_funcao()

##OUtro exemplo

def decoradora(valor):
    def imprime(*args):
        print("Multiplicação efetuada")
        return valor(*args)
    return imprime

@decoradora
def multiplica(a,b):
    return a * b

print(multiplica(2,3))



contador = 1
def contar_acessos(funcao_decorada):
    def nova_funcc(*args,**kwargs):
        global contador
        contador += 1
        return funcao_decorada(*args,**kwargs)
    return nova_funcc

@contar_acessos
def somar(a, b):
    return a + b

print(contador)
print(somar(2,2))
print(contador)


"""Crie uma função que faça a soma de 3 números e imprima em tela o resultado da
soma.
Crie um programa onde a função irá validar o nome e o CPF da pessoa estão
corretos baseados nos dados apresentados. Valide com retornos em tela se o CPF
está correto se o nome está correto.
Crie funções com argumentos *args e **kwargs e faça teste de saida dos
argumentos e execute o iterador for nos elementos.
Crie 2 funções onde 1 será a função decoradora e a outra irá receber a função
decorada. Teste pelo método decorado e pelo método através de variáveis
"""