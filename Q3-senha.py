#gardado o valor da senha 
senha = 1234
senhause = int(input("Digite a senha: "))
#o programa verificara se a senha esta correta caso nãe esteja aparecerar a mensagem senha incorreta e o programa pedirar para o usúario digitar novamente a senha  
while senhause != senha:
    print("Senha Invalida")
    senhause = int(input("Digite a senha: "))
#quando o usuário colocar a senha correta o programa finalizar
print("senha correta")