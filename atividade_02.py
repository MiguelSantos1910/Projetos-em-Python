contador = 0
while True:
    try:
        altura = float(input("Qual sua altura?"))
        peso = float(input("Qual seu peso?"))
        BMI = peso/altura**2
        print(f"Seu indíce BMI é de {BMI:.2f}")
        if BMI < 18.5:
            print("Você está abaixo do peso!")
        elif 18.5 <= BMI < 24.9:
            print("Você está normal!")
        elif 25 <= BMI < 29.9:
            print("Você está acima do peso!")
        elif 30 <= BMI < 34.9:
            print("Você está obeso!")
        if BMI >= 35:
            print("Você está em extrema obesidade!")
    except ValueError:
        print("Você digitou um caractere não numérico")
        print("Tente novamente!")
        contador += 1
        if contador == 1:
            print(f"Você tem apenas tentativas de digitação, digíte apenas caracteres numéricos!")
            print(f"Tentativa {contador}")
        if contador == 2:
            print(f"Você tem apenas 3 tentativas de digitação, digíte apenas caracteres numéricos!")
            print(f"Tentativa {contador}")
        if contador == 3:
            print(f"Você tem apenas 3 tentativas de digitação, digíte apenas caracteres numéricos!")
            print(f"Tentativa {contador}")
            break