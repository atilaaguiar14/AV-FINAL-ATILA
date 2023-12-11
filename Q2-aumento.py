# pedir para o usuario digitar o seu salario 
salario = float(input("digite seu salario"))
#o programa verificarar se o salário do usuario, se for menor que 400.00 o programa fara as ações pre programadas
if salario <= 400.00:
    print(f"Novo salário: {salario+(salario*(15/100)):.2f}")
    print(f"Reajuste ganho:{salario*(15/100):.2f}")
    print("Em percentual: 15 %")

#o programa verificarar se o salário do usuario, se for maior que 400.01 e menor que 800.00 o programa fara as ações pre programadas
elif salario >= 400.01 and salario <= 800.00:
    print(f"Novo salário: {salario+(salario*(12/100)):.2f}")
    print(f"Reajuste ganho:{salario*(12/100):.2f}")
    print("Em percentual: 12 %")

#o programa verificarar se o salário do usuario, se for maior que 800.01 e menor que 1200.00 o programa fara as ações pre programadas
elif salario >= 800.01 and salario <= 1200.00:
    print(f"Novo salário: {salario+(salario*(10/100)):.2f}")
    print(f"Reajuste ganho:{salario*(10/100):.2f}")
    print("Em percentual: 10 %")

#o programa verificarar se o salário do usuario, se for maior que 1200.01 e menor que 2000.00 o programa fara as ações pre programadas
elif salario >= 1200.01 and salario <= 2000.00:
    print(f"Novo salário: {salario+(salario*(7/100)):.2f}")
    print(f"Reajuste ganho:{salario*(7/100):.2f}")
    print("Em percentual: 7 %")

#o programa verificarar se o salário do usuario, se for maior que 2000.01 o programa fara as ações pre programadas
elif salario >  2000.01:
    print(f"Novo salário: {salario+(salario*(4/100)):.2f}")
    print(f"Reajuste ganho:{salario*(4/100):.2f}")
    print("Em percentual: 4 %")