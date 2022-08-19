print("Observação: use ponto para separar casa decimais e digite apenas uma casa decimal após o ponto!")
print('')
n1 = float(input("digite a primeira nota: "))
n2 = float(input("digite a segunda nota: "))
n3 = float(input("digite a terceira nota: "))
m = (n1+n2+n3)/3
print (f"Sua média é {round(m, 2)}")

if m >= 7:
    print("aprovado")
elif m == 10:
    print("aprovado com distinção!")
elif m < 7:
    print("reprovado")
else:
    print("Houve um problema para calcular a média, tente novamente!")
