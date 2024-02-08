'''
Exercícios sobre os comandos básicos em Python
'''

#1. Faça um programa que imprima o seu nome.
#print('João Otavio')
#2. Faça um programa que imprima o produto dos valores 30 e 27.
#print(30*27)
#3. Faça um programa que imprima a média aritmética entre os números 5, 8, 12.
#print((5+8+12)/3)

#4. Faça um programa que leia e imprima um número inteiro.
#numeroint = int(input("digite um numero inteiro"))
#print(numeroint)
#5. Faça um programa que leia dois números reais e os imprima.
#numero1 = float(input("digite um numero real:"))
#numero2 = float(input("digite outro numero real:"))
#print(numero1)
#print(numero2)

#6. Faça um programa que leia um número inteiro e imprima o seu
#   antecessor e o seu sucessor.
#numero = int(input('digite um numero inteiro'))
#print(f'sucessor: {numero+1}') 
#print(f'antecessor: {numero-1}') 

#7. Faça um programa que leia o nome o endereço e o telefone de
#   um cliente e ao final, imprima esses dados.
#nome = input('digite o seu nome:')
#print(nome)
#endereço = input('insia o seu endereço:')
#print(endereço)
#numerotelefone = input('insira o seu numero de telefone:')
#print(numerotelefone)

#8. Faça um programa que leia dois números inteiros e imprima a
#   subtração deles.
#numero1 = int(input('insira um numero inteiro'))
#numero2 = int(input('insira outro inteiro'))
#print(numero1-numero2)

#9. Faça um programa que leia um número real e imprima ¼ deste número.
#numero = float(input('digite um numero real'))
#print (numero/4)

#10. Faça um programa que leia três números reais e calcule a
#    média aritmética destes números. Ao final, o programa deve
#    imprimir o resultado do cálculo.
#num1 = float(input("digite o primeiro numero"))
#num2 = float(input("digite o segundo numero"))
#num3 = float(input("digite o terceiro numero"))
#print ((num1+num2+num3)/3)


#11. Faça um programa que leia dois números reais e calcule as
#    quatro operações básicas entre estes dois números, adição,
#    subtração,multiplicação e divisão. Ao final, o programa
#    deve imprimir os resultados dos cálculos.
#num1 = float (input('num1:'))
#num2 = float (input('num2:'))
#print (f"{num1} + {num2} = {num1+num2}")
#print (f"{num1} - {num2} = {num1-num2}")
#print (f"{num1} * {num2} = {num1*num2}")
#print (f"{num1} / {num2} = round{num1/num2}")


#12. Faça um programa que leia um número real e calcule o
#    quadrado deste número. Ao final, o programa deve
#    imprimir o resultado do cálculo.

#num1 = float(input('digite um numero real'))
#print(num1*num1)

#13. Faça um programa que leia o saldo de uma conta poupança
#    imprima o novo saldo, considerando um reajuste de 2%.

#conta = float(input("insira o valor da conta"))
#print  ("o novo valor da conta é:") 
#rint ((((2/100)*conta)+conta))

#14. Faça um programa que leia a base e a altura de um retângulo
#    e imprima o perímetro (base + altura) e a área (base * altura).

#base = float(input('insira o valor da base do retângulo'))
#altura = float(input('insira o valor da altura do retângulo'))
#print("o valor do perimetro é:")
#print (base+altura)
#print('o valorda área é:')
#print(base*altura)

#15. Faça um programa que leia o valor de um produto, o percentual
#    do desconto desejado e imprima o valor do desconto e o valor
#    do produto subtraindo o desconto.

#valorinteiro = float(input('insira o valor do produto'))
#esconto = float(input('insira o valor do desconto'))
#print('valor do {desconto:}')
#rint ((desconto/100)*valorinteiro)
#print('valor total do produto com desconto:')
#print  (valorinteiro-(valorinteiro * desconto/100))

#16. Faça um programa que calcule o reajuste do salário de um
#    funcionário. Para isso, o programa deverá ler o salário atual
#    do funcionário e ler o percentual de reajuste. Ao final imprimir
#    o valor do novo salário.

#salario = float(input('insira o valor do salario:'))
#reajuste = float(input('insira o a porcentagem de reajuste'))
#print ((reajuste/100*salario)+salario)

#17. Faça um programa que calcule a conversão entre graus centígrados
#    e Fahrenheit. Para isso, leia o valor em centígrados e calcule
#    com base na fórmula a seguir. Após calcular o programa deve
#    imprimir o resultado da conversão.
#    F = (9 * C + 160) / 5

#C = float(input('insira o valor de graus centígrados'))
#print ('o valor em fahrenheit é:')
#print ((9*C+160)/5)

#18. Faça um programa que calcule a quantidade de litros de combustível
#    consumidos em uma viagem, sabendo-se que o carro tem autonomia de
#    12 km por litro de combustível. O programa deverá ler o tempo
#    decorrido na viagem e a velocidade média e aplicar as fórmulas:
#    D = T x V       L = D / 12
#    Em que:
#    • D = Distância percorrida em horas
#    • T = Tempo
#    • V = Velocidade média
#    • L = Litros de combustível consumidos
#    Ao final, o programa deverá imprimir a distância percorrida e a
#    quantidade de litros consumidos na viagem.



#19. Faça um programa que calcule o valor de uma prestação em atraso.
#    Para isso, o programa deve ler o valor da prestação vencida, a
#    taxa periódica de juros e o período de atraso. Ao final, o
#    programa deve imprimir o valor da prestação atrasada, o período
#    de atraso, os juros que serão cobrados pelo período de atraso, o
#    valor da prestação acrescido dos juros. Considere juros simples.

vencida = float(input('insira o valor da prestação vencida:'))
juros = float(input("insira a porcentagem de juros:"))
atraso = float(input('insira o periodo de atraso:'))
print (vencida)
print (atraso)
print (juros"%")
print (juro*atraso)

#20. Faça um programa que efetue a apresentação do valor da conversão
#    em real (R$) de um valor lido em dólar (US$). Para isso, será
#    necessário também ler o valor da cotação do dólar.