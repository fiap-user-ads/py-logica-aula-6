"""
	DADA DUAS NOTAS PELO USUÁRIO, CALCULAR A MEDIA E VERIFICAR SE ELE ESTÁ
    APROVADO (MEDIA DE AO MENOS 6)
"""

# v.1
"""
# variáveis
n1 = float(input("Digite a nota 1: "))
n2 = float(input("Digite a nota 2: "))

media = (n1 + n2) / 2

# condições
if media >= 6:
    print(f"Aprovado com média {media}")
else:
    print(f"Reprovado com média {media}")
"""

# v.2 -> verificar se as notas são válidas
"""
# variáveis + verificação
n1 = float(input("Digite a nota 1: "))

if n1 >= 0 and n1 <= 10:
    n2 = float(input("Digite a nota 2: "))

    if n2 >= 0 and n2 <= 10:
        media = (n1 + n2) / 2

        if media >= 6 :
            print(f"Aprovado com média {media}")
        else:
            print(f"Reprovado com média {media}")
    else:
        print(f"Nota 2 inválida!")
else:
    print(f"Nota 1 inválida!")
"""

# v.3 -> caso o aluno não seja aprovado, verificar se ele tem a possibilidade de
# fazer recuperação (entre 4 e 5.9). Se sim, solicitar a nota de recuperação e calcular a
# nota final considerando a media com a nota de recuperação e verificar se ele passou (media 6)
"""

"""
n1 = float(input("Digite a nota 1: "))

if n1 >= 0 and n1 <= 10:
    n2 = float(input("Digite a nota 2: "))

    if n2 >= 0 and n2 <= 10:
        media = (n1 + n2) / 2

        if media >= 6 :
            print(f"Aprovado direto com média {media}")
        elif media >= 4 and media < 6:
            rec = float(input("Digite a nota da recuperação: "))

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
        print(f"Nota 2 inválida!")
else:
    print(f"Nota 1 inválida!")