# nota escola
"""
n1 = float(input("Digite a nota 1: "))

if n1 >= 0 and n1 <= 10:
    n2 = float(input("Digite a nota 2: "))

    if n2 >= 0 and n2 <= 10:
        n3 = float(input("Digite a nota 3: "))

        if n3 >= 0 and n3 < 10:
            menor = n1

            if(n2 < menor):
                menor = n2
            if(n3 < menor):
                menor = n3

            media = (n1 + n2 + n3 - menor) / 2

            if media >= 6 :
                print(f"Aprovado direto com média {media}")
            elif media >= 4 and media < 6:
                rec = float(input("Você ficou de recuperação... Digite a sua nota de recuperação: "))

                if rec >= 0 and rec <= 10:
                    media = (media + rec) / 2

                    if media >= 6:
                        print(f"Aprovado em recuperação com média {media}")
                    else:
                        print(f"Reprovado em recuperação com média {media}")
                else:
                    print(f"Nota de recuperação inválida!")
            else:
                print(f"Reprovado direto com média {media}")
        else:
            print(f"Nota 3 inválida!")
    else:
        print(f"Nota 2 inválida!")
else:
    print(f"Nota 1 inválida!")
"""

# 15
"""
n1 = float(input("Digite um numero: "))
n2 = float(input("Digite outro numero: "))
n3 = float(input("Digite mais um numero: "))

if (n1 == n2 and n2 == n3):
    print("Há 3 numeros iguais")
elif (n1 == n2 and n2 != n3):
    print("Há 2 numeros iguais")
elif (n1 != n2 and n2 == n3):
    print("Há 2 numeros iguais")
elif (n1 == n3 and n2 != n3):
    print("Há 2 numeros iguais")
else:
    print("Há 3 numeros diferente")
"""

# 16
"""
sal = float(input("Digite seu salário: R$"))
sexo = int(input("Informe seu sexo: \n[1] - Masculino \n[2] - Feminino \n"))
idade = int(input("Informe sua idade: "))

if sexo == 1:
    if(idade >= 0 and idade <= 20):
       valorConv = sal * 0.0534
    elif(idade > 20 and idade <= 40):
       valorConv = sal * 0.0844
    else:
       valorConv = sal * 0.1012
elif sexo == 2:
    if(idade >= 0 and idade <= 20):
        valorConv = sal * 0.0356
    elif(idade > 20 and idade <= 40):
        valorConv = sal * 0.0643
    else:
        valorConv = sal * 0.0802
else:
    print("erro --> sexo inválido")

print(f"O valor do convênio ficou de: R${valorConv:.2f}")
"""

# 17
"""
n1 = float(input("Digite a nota n1: "))
n2 = float(input("Digite a nota n2: "))
media = (n1 + n2) / 2 * 0.6

att = int(input("Digite a quantidade de atividade feitas [0 a 4]: "))

passou = media + att
if passou >= 6:
   print(f"Você passou com uma média de {passou:.2f}")
else:
    print(f"Você reprovou com uma média de {passou:.2f}")
"""

