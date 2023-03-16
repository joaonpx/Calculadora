print('\n     Calculadora\n')
value1 = input('Digite o primeiro valor: ')
value2 = input('Digite o segundo valor: ')

if value1.isdigit() == False or value2.isdigit() == False:
    print("Digite apenas números!")
    
    quit()

operationType = input('Digite a operação que quer fazer (+, -, /, *): ') 

if operationType == '+': 
  sum = float(value1) + float(value2)

  result = sum

  print(f'\nO resultado da operação é: {result}')

elif operationType == '-':
  sub = float(value1) - float(value2)

  result = sub

  print(f'\nO resultado da operação é: {result}')

elif operationType == '/':
  div = float(value1) / float(value2)

  result = div

  print(f'\nO resultado da operação é: {result:.2f}')

elif operationType == '*':
  mult = float(value1) * float(value2)

  result = mult

  print(f'\nO resultado da operação é: {result}')

else:
  print('\nOperação invalida!')
