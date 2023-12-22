while True:
  sequence = input('Informe os números da sequencia por virgula: ')

  try:
      numeros = [float(num) for num in sequence.split(',')]
      break  
  except ValueError:
      print('Erro: Certifique-se de inserir apenas números separados por vírgula. Tente novamente.')

order = sorted(numeros)

print('Os números escritos em ordem crescente ficam dessa forma:', order)

