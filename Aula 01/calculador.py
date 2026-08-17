# Para comentários de várias linhas usamos ''' '''
'''
    Aqui é um comentário de várias linhas.
    Isto também é chamando de DocString
    O que vamos fazer, uma calculadora simples:
    - pedimos o primeiro numero
    - pedimos o segundo numero
    - pedimos o operador
    - mostramos o resultado
'''
# para escrever na tela pode usar a ' ou "
print('************* Calculadora *************')
# agora vamos usar uma variavel para armazenar algo na memoria RAM
# variavel tem um nome e recebe um valor
# nome da variavel, sempre começando com letra, até 30 caracteres
# pode usar números e alguns simbolos
# python faz distinção de maiusculo e minusculo
# nomenclatura de nomes:
# camelCase, PascalCase, snake_case, kebab-case, lowercase, UPPERCASE
# primeiroNumero = 1
# PrimeiroNumero = 1
# primeiro_numero = 1
# primeiro-numero = 1
# primeironumero = 1
# PRIMEIRONUMERO = 1
primeiro_numero = input("Informe o primeiro número: ")
segundo_numero = input("Informe o segundo número: ")
operador = input('Informe o tipo de calculo " + - * / ": ')
# tomada de decisão
# para tomar decisão usamos o if
# para comparar igualdade use ==
if operador == "+":
    resultado = float(primeiro_numero) + float(segundo_numero)
elif operador == "-":
    resultado = float(primeiro_numero) - float(segundo_numero)
elif operador == "*":
    resultado = float(primeiro_numero) * float(segundo_numero)
elif operador == "/":
    resultado = float(primeiro_numero) / float(segundo_numero)
else:
    resultado = 0
    print("Você informou um operador que não existe!!!")
print(resultado)
