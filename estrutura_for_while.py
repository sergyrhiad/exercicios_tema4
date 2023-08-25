i = int (input('Qual a sua idade?'))
while (i >0):
 s = input('Qual o seu sexo? (M ou F).')
 if ((s == 'M') or (s =='m')):
  print(f'Boa noite, Senhor. Sua idade é {i}.')
 else:
   if ((s == 'F') or (s == 'f')):
    print(f'Boa noite, Senhora. Sua idade é {i}.')
   else:
    print('opção de sexo inexistente.')
    print('Tente novamente!')
 i = int(input('Qual a sua idade?'))
print('Encerrando...')