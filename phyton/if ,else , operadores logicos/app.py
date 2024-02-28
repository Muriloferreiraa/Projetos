 # APRENDENDO A USAR IF SOZINHO , BASTA COLOCAR E DPS FAZER UM PRINT
 # PARA VER SE É VERDADE OU  NÃO 

tenho_sede = True 
        
if tenho_sede:
    print("beber agua")

print("vida que segue")    

#----------------------
  #IF E ELSE SE O IF ESTIVER CORRETO APARECE O QUE ESTA NO PRINT
  #DO IF CASO AO CONTRARIO OCORRE O OPOSTO

esta_frio = False         
if esta_frio:
        print("vestir um casaco")
else:
        print("vestir camisa")        

#----------------------

#APRENDNENDO O OR(OU) AI VAI DEPENDER DO QUE VOCE ESCREVER 
 #NO IF E NO ELSE

tenho_sede = False             
tenho_fome = False      

if tenho_sede or tenho_fome:
    print("vou na cozinha")
else:
    print("vendo netflix")  
  
#------------------------
     
  #APRENDENDO AND(E) AS 2 COISAS TEM Q SER VERDADEIRO CASO CONTRARIO 
  # NÃO VAI PARA A OUTRA OPCÃO 

tenho_sede = False     
tenho_fome = True  

if tenho_sede and tenho_fome:
    print("fazer comida com coca")

else:
    print("dormir melhor")

#_---------------------

 #APRENDENDO O ELIF UMA MISTURA DE ELSE COM IF E O AND NOT E CASO VOCE
# QUERIA ALGUMA COISA E NÃO A OUTRA

tenho_sede = True      
tenho_fome = False 

if tenho_sede and tenho_fome:
    print("fazer comida e beber agua")

elif tenho_sede and not tenho_fome:
    print("beber agua")

elif tenho_fome and not tenho_sede:
    print("comer um viado")  

else:
    print("ficar deitado igual um idiota")

#=---------------------------------------
#operadores logicos  == igaul  != diferesntes > maior < meneor  
# <= menor ou igaul >= maior ou igual

num1 = 34
num2 = 32

if num1 == num2:
    print("num1 e igual a num2")

elif num1 != num2:
    print("difrentes")  
     
elif num1 > num2:
    print(" num1 maior")    

elif num1 < num2:
    print(" num2 maior")        