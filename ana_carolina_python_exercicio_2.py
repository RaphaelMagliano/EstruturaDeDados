while True:
    nota= float(input("Digite uma nota: "))
    if nota > 10 or nota < 0:
        print("Por favor, digite um valor válido!")
        continue
    else:
        print("Valor válido, obrigado!")
        break



