# while não tem segredo basta não fazer looping infinito que ta tudo certo
 
i = 1 

while i < 10:
    print(i)
    i += 1
print("terminou")

#----------------

criancas = ["vit","fabi","manu"]

for item in criancas:
    print(item)

canal = "meu zovo"

for letra in canal :
    print(letra)

#-----------

#Primeiro parametro(6) é onde eu quero que inicie/ o segundo(20) onde termina/o terceiro(2)
#em quantos em quantos numeros eu quero que ele pule
#unico obrigatorio é o segundo(20)
 
for index in range(6,20,2):
    print(index)

#-----------------------

criancas = ["gabi","manu","sofia"]

for index in range(len(criancas)):
    print(criancas[index],index)

 #--------------------------------

for index in range(5):
    if index ==0:
        print("primeiro linha")
    else:
        print(f"outras linhas {index}")

#---------------------

matrix_numeros = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0],
]
for linha in matrix_numeros:
    # print(linha)
    print("---")
    for coluna in linha:
        print(coluna)