#NÃO ACEITA VALOR DUPLICADO 

meses ={
    "jan":"Janeiro",
    "fev":"Fevereiro",
    "mar":"Marco",
    "abr":"Abriu",
    "mai":"Maio",
    "jun":"Junho",
    "jul":"JUlho",
    "ago":"Agosto",

}
print(meses["fev"])#da erro caso n tenho
print(meses.get("ma","fev"))#caso n tenha aparece nenhum ou valor padrao
print(len(meses))#quantidade de resultados 