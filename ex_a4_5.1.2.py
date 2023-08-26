print('Primos de 2 a 99:')
for n in range(2,100):
  #variavel que altera seu valor caso o nª não seja primo.
  nao_primo = 0
  for x in range(2,n):
    #o nª for divisivel qualquer valor, não é primo 
    if n % x == 0 :
      nao_primo = 1
      #caso encontre um valor divisivel ja faz um break
      #assim não precisa testar ate o final sem necessidade 
      break
  if not nao_primo :
    print(n)  