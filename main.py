while True:
  sequence = input('Enter the sequence of numbers separated by commas: ')

  try:
      numbers = [float(num) for num in sequence.split(',')]
      break
  except ValueError:
      print('Error: Make sure to enter only numbers separated by commas. Please try again.')

sorted_numbers = sorted(numbers)

print('The numbers in ascending order are:', sorted_numbers)


