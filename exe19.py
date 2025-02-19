# 19. Faça um programa que receba duas notas de seis alunos. Calcule e mostre:
# - A média aritmética das duas notas de cada aluno; e
# - A mensagem que está na tabela a seguir:
#       Média Aritmética | Mensagem
#       Até 3 | Reprovado
#       Entre 3 e 7  | Exame
#       De 7 para cima | Aprovado
# - O total de alunos aprovados;
# - O total de alunos de exame;
# - O total de alunos reprovados;
# -  A média da classe.


#while #enquanto

contAlunos = 1 #inicializa a contagem de alunos
qtdAlunos = 6 #inserir a quantidade de alunos a serem contatos
qtdNotas = 2 #inserir a quantidade de notas
qtdAprovados = 0
qtdReprovados = 0
qtdExame = 0
somaMedias = 0

while contAlunos <= qtdAlunos:
    print("\n") #Imprimi ou pula linha no console
    print("################################")
    print(f"Aluno {contAlunos}")
    
    notaum = int(input("Insira a primeira nota do aluno: "))
    notadois = int(input("Insira a segunda nota do aluno: "))

    media = notaum+notadois/qtdNotas
    somaMedias += media

    if media < 3:
        print("Reprovado")
        qtdReprovados += 1
    elif media >= 3 and media < 7:
        print("Exame")
        qtdExame += 1
    elif media >= 7:
        print("Aprovado")
        qtdAprovados += 1

    contAlunos += 1 #contAlunos = contAlunos+1

mediaClasse = somaMedias/qtdAlunos
    
print("\n") #Imprimi ou pula linha no console
print("################################")    
print("Resumo clase: ")
print(f"Alunos Reprovados: {qtdReprovados}")
print(f"Alunos Aprovados: {qtdAprovados}")
print(f"Alunos Exames: {qtdExame}")
print(f"A media da classe foi de: {mediaClasse}")
