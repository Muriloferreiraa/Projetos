def big_mac(): # FUNCOES PASSO A PASSO(PARA CRIAR UMA FUNCAO SE USA DEF / NOME DA FUNCAO SE TIVER ATRIBUTO COLOCA)
    print("sanduiche big mac")  #TEM QUE ESTRAR COM TAB TUDO O QUE TIVER DENTRO DO TAB É UMA FUNCAO 
print("inicio")                     #PODE PASSAR MAIS DE 1 ATRIBUTO /PODE CRIAR UMA FUNCAO COM OUTRAS FUNCOES JÁ CRIADA
big_mac()                            
print("fim")


def fazer_big_mac(nome):
     print(f"sanduiche big {nome}")

fazer_big_mac("murilo")
fazer_big_mac("vitroia")
fazer_big_mac("gabriel")     

def fazer_batata(tamanho):
       print(f"batata {tamanho}")

def preparar_refrigante(tipo,tamanho):
        print(f"{tipo} {tamanho}")
           
fazer_big_mac("murilo")
fazer_batata("grande")
preparar_refrigante("coca","grande")


def fazer_combo_big_mac(nome,tamanho_batata,taanho_refri):
      fazer_big_mac(nome)
      fazer_batata(tamanho_batata)
      preparar_refrigante(taanho_refri)

      fazer_combo_big_mac("murilo","grande","grande") #FIM DAS FUNCOES PASSO A PASSO 


def soma_num(num1,num2):  #SOMA DE NUMEROS #PODE CRIAR UMA FUNCAO E RETORNANDO O RESULTADO DELA fora da funcao
    return num1+num2                    #igual podemos ver no explo
resultado = soma_num(15,20)
print(resultado)

def maior_num(lista_num):
    lista_num.sort()
    lista_num.reverse()
    maior_num=lista_num[0]
    return maior_num

resultado=maior_num([23,42,-542,7,0,1,2])
print(resultado)