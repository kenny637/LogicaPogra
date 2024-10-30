nome=str(input("informe um nome: "))
lernome=len(nome)
if(lernome<=3):
    print("valido")
else:
    print("invalido")
idade=int(input("informe sua idade: "))
if(idade>=0)and(idade<=150):
    print("valido")
else:
    print("invalido")
salario=int(input("informe seu salario: "))
if(salario>0):
    print("valido")
else:
    print("invalido")
genero=str(input("informe seu sexo: "))
if(genero=="f")or(genero=="m"):
    print("valido")
else:
    print("invalido")
estadocivil=str(input("informe seu estado civil: "))
if(estadocivil=="s")or(estadocivil=="c")or(estadocivil=="v")or(estadocivil=="d"):
    print("valido")
else:
    print("invalido")
print('Seu nome é',nome)
print('Sua idade é',idade)
print('Seu salario é',salario)
print('genero:',genero)
print('Seu estado civil',estadocivil)