from calc import sum, sub, mult, div

print('\n     Calculadora\n')
value1 = input('Digite o primeiro valor: ')
value2 = input('Digite o segundo valor: ')

if value1.isdigit() == False or value2.isdigit() == False:
    print("Digite apenas números!")
    
    quit()

operationType = input('Digite a operação que quer fazer (+, -, /, *): ') 

if operationType == '+': 
  result = sum(value1, value2)

  print(f'\nO resultado da operação é: {result}')

elif operationType == '-':
  result = sub(value1, value2)

  print(f'\nO resultado da operação é: {result}')

elif operationType == '/':
  result = div(value1, value2)

  print(f'\nO resultado da operação é: {result:.2f}')

elif operationType == '*':
  result = mult(value1, value2)

  print(f'\nO resultado da operação é: {result}')

else:
  print('\nOperação invalida!')
