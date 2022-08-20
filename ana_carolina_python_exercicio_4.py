import calendar

ano = int(input("Digite um ano para verificar se é bissexto: "))
bissexto = calendar.isleap(ano)
if bissexto == True:
    print(f"{ano} é um ano bissexto")
else:
    print(f"{ano} não é um ano bissexto")

