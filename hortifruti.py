pergunta = input("Deseja caucular a compra do cliente? (sim/não) ").strip().lower()

while (pergunta != "não") and (pergunta != "nao"):
    if pergunta == "sim":
        try:
            print("📝 Tabela de preços por Kg:\n🍓 Morango até 5 Kg: R$2,50\n🍓 Morango acima de 5 Kg: R$2,20\n🍎 Maçã até 5 Kg: R$1,80\n🍎 Maçã acima de 5 Kg: R$1,50")
            while True:
                maca = int(input("Digite a quantidade (em Kg) de maçãs: ").strip())
                if maca >= 0:
                    break
                else:
                    print("Você precisa digitar um valor de frutas maior ou igual a 0!")
            
            while True:
                morango = int(input("Digite a quantidade (em Kg) de morangos: ").strip())
                if morango >= 0:
                    break
                else:
                    print("Você precisa digitar um valor de frutas maior ou igual a 0!")
            
            totalKilos = maca + morango

            if totalKilos <= 5:
                valorTotal = (maca * 1.80) + (morango * 2.50)
            else:
                valorTotal = (maca * 1.50) + (morango * 2.20)

            if (totalKilos > 8) or (valorTotal > 25):
                print("Ao comprar mais de 8Kg ou R$25,00 de frutas o cliente ganha 10% de desconto!")
                print(f"Valor total a pagar com o desconto de 10% é igual a: R${valorTotal - (valorTotal*0.10):.2f}")
            else:
                print(f"Total a pagar: {valorTotal:.2f}")
            
        except ValueError:
            print("Algo deu errado, por favor digite apenas a quantidade inteira de frutas!")
    else:
        print("Por favor digite apenas sim ou não!")
    
    print(100*"-")
    pergunta = input("Deseja calcular a compra do clilente? (sim/não) ").strip().lower()

print("Programa finalizado!")
            



