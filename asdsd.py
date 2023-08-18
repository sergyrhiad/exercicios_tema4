print('Bem vindo a Loja do Sérgy Rhiad Ribas Fagundes')
vp = float(input('Digite o valor do produto: $'))
qtd = int(input('Digite o quantidade do produto: '))
if 0 < qtd < 200:
  # Percentual de desconto 0%
  vt= (qtd*vp)
  print('desconto de 0%.')
  print(f'O valor SEM desconto é de ${vt:.2f}')
  print(f'O valor COM desconto é de ${vt:.2f}')
elif 200 <= qtd < 1000:
  # Percentual de desconto 5%
  vt = qtd * vp
  des = (5/100) * vt
  print('desconto de 5%.')
  print('O valor SEM desconto é de $.' .format(qtd*vp))
  print('O valor COM desconto é de {:.2f}$.' .format(vt-des))
elif 1000 < qtd < 2000:
  # Percentual de desconto 10%
  vt = (qtd*vp)
  des = (10/100) * vt
  print('desconto de 10%.')
  print('O valor SEM desconto é de {:.2f}$.' .format(qtd*vp))
  print('O valor COM desconto é de {:.2f}$.' .format(vt-des))
elif qtd > 2000:
  # Percentual de desconto 15%
  vt =  (qtd*vp)
  des= (15/100) * vt
  print('desconto de 15%.')
  print('O valor SEM desconto é de {:.2f}$.' .format(qtd*vp))
  print('O valor COM desconto é de {:.2f}$.' .format(vt-des))
else:
  print('VALOR NÃO ACEITO!')
  print('TENTE NOVAMENTE!\n')
print('OBRIGADO, VOLTE SEMPRE!!!')
print('AGRADECEMOS SUA VISITA!!!')