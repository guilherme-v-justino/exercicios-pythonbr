"""Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre,
e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:

      Média de Aproveitamento  Conceito
      Entre 9.0 e 10.0        A
      Entre 7.5 e 9.0         B
      Entre 6.0 e 7.5         C
      Entre 4.0 e 6.0         D
      Entre 4.0 e zero        E

      Algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e
      a mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E. """

nota1 = float(input("Digite a primeira nota parcial: "))
nota2 = float(input("Digite a segunda nota parcial: "))
conceito = ' '
aprovacao = ' '
media = (nota1 + nota2) / 2
if 0 <= media <= 10:
    if 0 <= media < 4:
        conceito = 'E'
        aprovacao = 'REPROVADO'
    if 4 <= media < 6:
        conceito = 'D'
        aprovacao = 'REPROVADO'
    if 6 <= media < 7.5:
        conceito = 'C'
        aprovacao = 'APROVADO'
    if 7.5 <= media < 9:
        conceito = 'B'
        aprovacao = 'APROVADO'
    if 9 <= media <= 10:
        conceito = 'A'
        aprovacao = 'APROVADO'
    print("Média de Aproveitamento      Conceito        Situação")
    print(f'         {media:.1f}                    {conceito}            {aprovacao}')
else:
    print("Notas Inválidas")




