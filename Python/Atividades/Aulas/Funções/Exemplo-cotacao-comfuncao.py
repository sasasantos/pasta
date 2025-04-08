import Funcoes

while True: 
    Funcoes.limpar_tela()
    print ("Conversor de Moedas")

    cotacao_dolar = Funcoes.obter_cotacao()

    print("\nEscolha:")
    print("[1] - Converter Dólar para Real")
    print("[2] - Converter Real para Dólar")

    opcao = int(input("Digite um número para conversão: "))

    if opcao == 1:
        resultado = Funcoes.converter_dolar_para_real (cotacao_dolar)
        print(f"O valor convertido em Reais é: R$ {resultado:.2f}")

    elif opcao == 2:
        resultado = Funcoes.converter_real_para_dolar (cotacao_dolar)
        print(f"O valor convertido em Dólares é: $ {resultado:.2f}")

    else:
        print("Opção inválida. Escolha 1 ou 2.")

    input("Pressione <Enter> para continuar ...")