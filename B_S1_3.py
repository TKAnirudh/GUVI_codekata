x = input()

if x.isalpha():
  if x in ['A','E','I','O','U','a','e','i','o','u']:
    print('Vowel')
  else:
    print("Consonant")
else:
  print('invalid')
