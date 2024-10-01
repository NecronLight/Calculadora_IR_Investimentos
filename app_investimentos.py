#Pede para que o usuário informe um tipo de investimento entre as opções apresentadas
tipo_investimento = int(input("Informe o número correspondente ao tipo de investimento (1- CDB, 2- LCI, 3- LCA): "))

if tipo_investimento == 1:
    print("O investimento escolhido foi CDB")

elif tipo_investimento == 2:
    print("O investimento escolhido foi LCI")

elif tipo_investimento == 3:
    print("O investimento escolhido foi LCA")

else:
    print("Investimento inválido")
    exit()

#Pede para que o usuário informe o valor a ser resgatado.
while True:
    try:
        valor_resgate = float(input("Informe o valor em reais a ser resgatado R$: ")) #Converte o número em float
        print("Valor a ser resgatado R$ {:.2f}: ".format(valor_resgate))
        break


    except ValueError: #Caso o usuário não informe um valor que possa ser convertido em float, será informado que o valor é inválido
        print("Valor inválido. Insira o valor em reais. Exemplo: 150 ou 150.00")

#Pede para que o usuário informe o valor a ser resgatado.
while True:
    try:
        dias_investido = int(input("Agora informe o número de dias em que o valor ficou investido: "))
        print("O número de dias em que o valor ficou investido é:", dias_investido,"dias")
        break

    except ValueError: #Caso o usuário não informe um valor 'inteiro', será informado que o valor é inválido
        print("Quantidade de dias informada incorreta. Informe um número inteiro por favor")

#Resultado informando a alíquota aplicada e valor a ser pago como imposto com base no número de dias de investimento
if dias_investido <= 180:
    print("Alíquota de 22,5% de IR")
    print("")
    valor_ir = valor_resgate * 0.225
    print("Valor do imposto de renda a ser pago R$ {:.2f}: ".format(valor_ir))

elif dias_investido > 180 and dias_investido <= 360:
    print("Alíquota de 20% de IR")
    print("")
    valor_ir = valor_resgate * 0.2
    print("Valor do imposto de renda a ser pago R$ {:.2f}: ".format(valor_ir))

elif dias_investido > 360 and dias_investido <= 720:
    print("Alíquota de 17,5% de IR")
    print("")
    valor_ir = valor_resgate * 0.175
    print("Valor do imposto de renda a ser pago R$ {:.2f}: ".format(valor_ir))

else:
    print("Alíquota de 15% de IR")
    print("")
    valor_ir = valor_resgate * 0.15
    print("Valor do imposto de renda a ser pago R$ {:.2f}: ".format(valor_ir))

