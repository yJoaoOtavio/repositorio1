'''
Exercícios sobre os comandos de condição em python
'''

#1. Faça um programa que leia dois valores numéricos inteiros e efetue
#   a adição, caso o resultado seja maior que 10, apresentá-lo.
def q01():
    num1 = int(input('Primeiro número: '))
    num2 = int(input('Segundo número: '))
    soma = num1+num2
    if soma > 10:
        print(f'Soma: {soma}')

#2. Faça um programa que leia dois valores inteiros e efetue a adição.
#   Caso o valor somado seja maior que 20, este deverá ser apresentado
#   somando-se a ele mais 8, caso o valor somado seja menor ou igual a
#   20, este deverá ser apresentado subtraindo-se 5.
def q02():
    num1 = int(input('Primeiro número: '))
    num2 = int(input('Segundo número: '))
    soma = num1+num2
    if soma > 20:
        print(f'Resultado: {soma+8}')
    else:
        print(f'Resultado: {soma-5}')

#3. Faça um programa que leia um número e imprima uma das duas mensagens:
#   "É múltiplo de 3"ou "Não é múltiplo de 3".
def q03():
   num = int(input('insira um numero inteiro:'))
   resul = num % 3
   if resul == 0:
     print ('é multiplo de 3')
   else :
         print('não é multiplo de 3')
     


#4. Faça um programa que leia um número e informe se ele é ou não divisível por 5.
def q04():
    num = int(input('insira um numero inteiro:'))
    resul = num % 5
    if resul == 0:
       print ("é divisivel por 5")
    else : 
        print('não é divisivel por 5')



#5. Faça um programa que leia um número e informe se ele é divisível por 3 e por 7.
def q05():
    num = int(input('insira um numero inteiro'))
    if num % 3 == 0 :
      if num % 7 == 0 :
         print (num)
         print('é divisivel')
         

#6. A prefeitura do Rio de Janeiro abriu uma linha de crédito para os funcionários
#   estatutários. O valor máximo da prestação não poderá ultrapassar 30% do salário
#   bruto. Faça um programa que permita entrar com o salário bruto
#   e o valor da prestação e informar se o empréstimo pode ou não ser concedido.
def q06():

    Salario = float(input('insira o valor do salario:'))
    prestação = float(input('insira o valor da prestação:'))
    valormax = (30*Salario)/100
    if prestação>(valormax):
        print ('valor de prestação invalido.')
    else :
        print ('valor de prestação valido!')

#7. Faça um programa que leia um número e indique se o número está compreendido
#   entre 20 e 50 ou não.
def q07():

    num = int(input('insira um numero inteiro'))
    if num > 20 and num <50:
        print (f"{num} é compreendido")
    else:
        print (f'{num} não é compreendido')

#8. Faça um programa que leia um número e imprima uma das mensagens:
#   "Maior do que 20", "Igual a 20"ou "Menor do que 20".
def q08():

    num = int(input("insira um numero inteiro:"))
    if num > 20 :
        print (" numero é maior que 20")
    elif num == 20:
        print ("numero igual a 20")
    else:
        print ('numero Menor que 20') 
       

#9. Faça um programa que permita entrar com o ano de nascimento da pessoa e com o
#   ano atual. O programa deve imprimir a idade da pessoa. Não se esqueça de
#   verificar se o ano de nascimento informado é válido.
def q09():

    anonascimento = int(input('insira seu ano de nascimento:'))
    anoatual = 2024
    if num > 2024:
     print ("o ano inserido é invalido!")
    else:
        print (f'Sua idade é:{anoatual - num}')



#10. Faça um programa que leia três números inteiros e imprima os três em ordem
#crescente.
def q10():

    a = int(input('1 numero:'))
    b = int(input('1 numero:'))
    c = int(input('1 numero:'))
    if a<b and b<c:
        print (f'{a}, {b}, {c}')
    if a<b and b<c:
        print (f'{a}, {c}, {b}')
    if a<b and b<c:
        print (f'{b}, {a}, {c}')        
    if a<b and b<c:
        print (f'{a}, {b}, {c}')
    if a<b and b<c:
        print (f'{a}, {b}, {c}') 
    if a<b and b<c:
        print (f'{a}, {b}, {c}')   

#11. Faça um programa que leia 3 números e imprima o maior deles.



#12. Faça um programa que leia a idade de uma pessoa e informe:
#• Se é maior de idade
#• Se é menor de idadea
#• Se é maior de 65 anos

#13. Faça um programa que permita entrar com o nome, a nota da prova 1 e a nota
#da prova 2 de um aluno. O programa deve imprimir o nome, a nota da prova 1,
#a nota da prova 2, a média das notas e uma das mensagens: "Aprovado",
#"Reprovado"ou "em Prova Final"(a média é 7 para aprovação, menor que 3 para
#reprovação e as demais em prova final).

#14. Faça um programa que permita entrar com o salário de uma pessoa e imprima o
#desconto do INSS segundo a tabela seguir:
#Salário Faixa de Desconto
#Menor ou igual à R$600,00 Isento
#Maior que R$600,00 e menor ou igual a R$1200,00 20%
#Maior que R$1200,00 e menor ou igual a R$2000,00 25%
#Maior que R$2000,00 30%

#15. Um comerciante comprou um produto e quer vendê-lo com um lucro de 45% se o
#valor da compra for menor que R$20,00, caso contrário, o lucro será de 30%.
#Faça um programa que leia o valor do produto e imprima o valor da venda.

#16. A confederação brasileira de natação irá promover eliminatórias para o
#próximo mundial. Faça um programa que receba a idade de um nadador e imprima
#a sua categoria segundo a tabela a seguir:
#Categoria Idade
#Infantil A 5 - 7 anos
#Infantil B 8 - 10 anos
#Juvenil A 11 - 13 anos
#Juvenil B 14 - 17 anos
#Sênior maiores de 18 anos

#17. Depois da liberação do governo para as mensalidades dos planos de saúde,
#as pessoas começaram a fazer pesquisas para descobrir um bom plano, não
#muito caro. Um vendedor de um plano de saúde apresentou a tabela a seguir.
#Faça um programa que entre com o nome e a idade de uma pessoa e imprima o
#nome e o valor que ela deverá pagar.
#Idade Valor
#Até 10 anos R$30,00
#Acima de 10 até 29 anos R$60,00
#Acima de 29 até 45 anos R$120,00
#Acima de 45 até 59 anos R$150,00
#Acima de 59 até 65 anos R$250,00
#Maior que 65 anos R$400,00

#18. Faça um programa que leia um número inteiro entre 1 e 12 e escreva o mês
#correspondente. Caso o usuário digite um número fora desse intervalo, deverá
#aparecer uma mensagem informando que não existe mês com este número.

#19. Em um campeonato nacional de arco-e-flecha, tem-se equipes de três jogadores
#para cada estado. Sabendo-se que os arqueiros de uma equipe não obtiveram o
#mesmo número de pontos, criar um programa que informe se uma equipe foi
#classificada, de acordo com a seguinte especificação:
#• Ler os pontos obtidos por cada jogador da equipe;
#• Mostrar esses valores em ordem decrescente;
#• Se a soma dos pontos for maior do que 100, imprimir a média aritmética entre eles,
#  caso contrário, imprimir a mensagem "Equipe desclassificada".

#20. O banco XXX concederá um crédito especial com juros de 2% aos seus clientes de
#acordo com o saldo médio no último ano. Faça um programa que leia o saldo médio
#de um cliente e calcule o valor do crédito de acordo com a tabela a seguir.
#O programa deve imprimir uma mensagem informando o saldo médio e o valor de
#crédito.
#Saldo Médio Percentual
#de 0 a 500 nenhum crédito
#de 501 a 1000 30% do valor do saldo médio
#de 1001 a 3000 40% do valor do saldo médio
#acima de 3001 50% do valor do saldo médio

#21. A biblioteca de uma Universidade deseja fazer um programa que leia o nome do
#livro que será emprestado, o tipo de usuário (professor ou aluno) e possa
#imprimir um recibo conforme mostrado a seguir. Considerar que o professor
#tem dez dias para devolver o livro e o aluno só três dias.
#• Nome do livro:
#• Tipo de usuário:
#• Total de dias:

#22. Construa um programa que leia o percurso em quilômetros, o tipo do carro e
#informe o consumo estimado de combustível, sabendo-se que um carro tipo A faz
#12 km com um litro de gasolina, um tipo B faz 9 km e o tipo C 8 km por litro.

#23. Crie um programa que informe a quantidade total de calorias de uma refeição
#a partir da escolha do usuário que deverá informar o prato, a sobremesa, e
#bebida conforme a tabela a seguir.
#Prato  Sobremesa   Bebida
#Vegetariano 180cal Abacaxi 75cal   Chá 20cal
#Peixe 230cal   Sorvete diet 110cal Suco de laranja 70cal
#Frango 250cal  Mousse diet 170cal  Suco de melão 100cal
#Carne 350cal   Mousse chocolate 200cal Refrigerante diet 65cal
def q23():
    prato = input('prato: ').upper().strip()
    sobremesa = input('sobremesa: ').upper().strip()
    bebida = input('bebida: ').upper().strip()

    total = 0
    total += 180 if prato == 'VEGETARIANO' else 0
    total += 230 if prato == 'PEIXE' else 0
    total += 250 if prato == 'FRANGO' else 0
    total += 350 if prato == 'CARNE' else 0
    total += 75 if sobremesa == 'ABACAXI' else 0
    total += 110 if sobremesa == 'SORVETE DIET' else 0
    total += 170 if sobremesa == 'MOUSSE DIET' else 0
    total += 200 if sobremesa == 'SORVETE DE CHOCOLATE' else 0
    total += 20 if bebida == 'CHA' else 0  
    total += 70 if bebida == 'SUCO DE LARANJA' else 0  
    total += 100 if bebida == 'SUCO DE MELAO' else 0  
    total += 65 if bebida == 'REFRIGERANTE' else 0  

    print (f'total de calorias:{total}')

#24. A polícia rodoviária resolveu fazer cumprir a lei e vistoriar veículos para
#cobrar dos motoristas o DUT. Sabendo-se que o mês em que o emplacamento do
#carro deve ser renovado é determinado pelo último número da placa do mesmo,
#faça um programa que, a partir da leitura da placa do carro, informe o mês
#em que o emplacamento deve ser renovado.
def q24():

    placa = input('placa do veiculo: ').upper().strip()
    mes = placa[len(placa)-1]
    if placa = 1:
        print('janeiro')
    elif placa = 2 fevereiro
    print ('')    


#25. A prefeitura contratou uma firma especializada para manter os níveis de
#poluição considerados ideais para um país do 1º mundo. As indústrias,
#maiores responsáveis pela poluição, foram classificadas em três grupos.
#Sabendo-se que a escala utilizada varia de 0,05 e que o índice de poluição
#aceitável é até 0,25, fazer um programa que possa imprimir intimações de
#acordo com o índice e a tabela a seguir:
#Índice Indústrias que receberão intimação
#0,3 1º grupo
#0,4 1º e 2º grupos
#0,5 1º, 2º e 3º grupos

opcao = int(input('Questão a ser executada: '))
match opcao:
    case 1: q01()
    case 2: q02()
    case 3: q03()
    case 4: q04()
    case 5: q05()
    case 6: q06()
    case 7: q07()
    case 8: q08()
    case 9: q09()
    case 10: q10()
    case 23: q23()
    case 24: q24()
    case _: print('Opção Inválida!')