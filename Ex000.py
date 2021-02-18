#Ex001: faça um programa que digite "Olá, Mundo" na tela.
print('Olá, Mundo!')

#Ex002:
nome = input('Digite o seu nome: ')
print('Bom dia, o seu nome é', nome)

#Ex003: faça um algoritimo que some dois valores.
n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
s = n1 + n2
print('A soma de {} mais {} é {}! '.format(n1, n2, s))

#Ex004: crie um programa que leia uma variavel qualquer e defina seu tipo primitivo, se esta em maisculas, e se é numerico.
a = input('Digite algo: ')
print(a,'o tipo primitivo é', type(a))
print(a,'esta em maiusculas? ',a .isupper())
print(a,'é numerico? ',a. isnumeric())

#Ex005: faça um programa que leia um numero e mostre o seu sucessor e antecessor.
n = int(input('Digite um numero: '))
suc = n + 1
ant = n - 1
print('O sucessor de seu numero é {}!'.format(suc))
print('O antecessor de seu numero é {}!'.format(ant))

#Ex006: crie um algoritimo que leia o seu numero e mostre o dobro o triplo e a raiz quadrada.
n = int(input('Digite um valor: '))
d = n * 2
t = n * 3
r = n **(1/2)
print('O dobro de seu numero é {}, o triplo é {}, e  raiz quadrada é {}! '.format(d, t, r))

#Ex007: faça um programa que calcule a media de um aluno
m1 = int(input('Entre com a primeira media: '))
m2 = int(input('Entre com a segunda media: '))
print('A media final do aluno é {}!'.format((m1 + m2) / 2))

#Ex008: faça um programa que leia um valor em metros e converta-o em centimetros e milimetros.
m = int(input('Entre com a quantidade de metros: '))
cm = m * 100
mm = cm * 10
print('{} m em cm é {}, e em mm é {}.'.format(m, cm, mm))

#Ex009: faça um programa que leia um numero inteiro qualquer e mostre sua tabuada.
t = int(input('Digite um numero inteiro qualquer: '))
t1 = [t * 0, t * 1, t * 2, t * 3, t * 4, t * 5, t * 6, t * 7, t * 8, t * 9, t * 10]
print(t1)

#Ex0010: crie um algoritimo que leia quanto a pessoa tem em reais e converta em dolares.
r = float(input('Insira a quantidade de reais: '))
d = r * 0.19
print('Você possui {} dolares.'.format(d))

#Ex0011: faça um programa que leia a largura e a altura de uma parede em metros.
#Calcule a sua aréa e a quantidade de tinta para pinta-la, sabende que um litro de tinta pinta 2m².
alt = float(input('Entre com a altura de sua parede: '))
lag = float(input('Entre com a largura de sua parede: '))
met = alt + lag
area = alt * lag
tinta = met / 2
print('Sua parede possui {} de m², e {} de aréa. Para pintala serão necessarios {} de litros de tinta. '.format(met, area, tinta))

#Ex0012: faça um programa que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
v = float(input('Insira o preço do produto: '))
v1 = v * (5/100)
vf = v - v1
print('O preçe final do produto é de: {}'.format(vf))

#Ex0013: faça um programa que leia um salario de um funcionario e mostre seu novo salario com 15% de aumento.
s = float(input('Entre com o salario '))
s1 = s *(15/100)
s2 = s + s1
print('O aumento será de {}, o valor do salario atual é de {}.'.format(s1, s2))

#Ex0014: faça um programa que converta a temperatura de celsius para fahrenheit.
c = float(input('Informe a temperatura em C: '))
f = 9 * c / 5 + 32
print('A temperatura de {}C, corresponde a {}F! '.format(c, f))

#EX0015: Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele alugado.
#Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0.15 por Km rodado.
dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos Km rodados? '))
pago = (dias * 60) + (km * 0.15)
print('O total a pagar é de R${:.2f}'.format(pago))















