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