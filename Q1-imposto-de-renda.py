#Pedir para o usario digita o salário 
salario = float(input("digite seu salario"))
# o programa verificarar se o salário do usuario, se for menor que 2000.00 o programa dirar que ele está isento 
if salario <= 2000.00:
    print('você esta isento')
# o programa verificarar se o salário do usuario, se for maior que 2000.01 e menor que 3000.00 o programa dirar o tanto de imposto que é necessário pagar
elif salario >= 2000.01 and salario <= 3000.00:
   imposto = salario*0.08
   print(f'R${imposto}')
#o programa verificarar se o salário do usuario, se for maior que 3000.01 e menor que 4500.00 o programa dirar o tanto de imposto que é necessário pagar
elif salario >= 3000.01 and salario <= 4500.00:
   imposto = salario*0.18
   print(f'R${imposto}')
# # o programa verificarar se o salário do usuario, se for maior que 4500.00 o programa dirar o tanto de imposto que é necessário pagar
elif salario > 4500.00:
   imposto = salario*0.28
   print(f'R${imposto:.2f}')