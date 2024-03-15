print('#'*20)
print(' '*3,'menu de opçoes')
print('#'*20)
while True:
    opcao = int(input('[1] para cadastrar um novo produto\n[2] para alterar os dados de algum produto\n[3] para listar os produtos\nDigite aqui: '))
    if opcao == 1:
        nome_do_produto = str(input('Digite o nome do pruduto: '))
        cod_do_produto = str(input('digite o codigo do produto: '))
        custo_do_produto = float(input('digite o custo do produto: : '))
        custo_fixo = int(input('digite o custo fixo do produto: '))
        comissao_de_venda = int(input('qual a comissão de venda: '))
        imposto_sobre_venda = int(input('digite o imposto sobre venda: '))
        margem_de_lucro = float(input('digite o imposto sobre venda: '))
        preco_de_vendap1 = (((custo_fixo)/100) + ((comissao_de_venda)/100) + ((imposto_sobre_venda)/100) + ((margem_de_lucro)/100)/(100/100))
        preco_de_vendap2 = custo_do_produto / (1 - preco_de_vendap1)
        print(f"O preço de venda do seu roduto será de:{float(preco_de_vendap2):.2f}R$")
        confirmacao = str(input("produto cadastrado. deseja voltar para o menu? S/N: "))
        if confirmacao == "s" or "S":
            continue
        elif confirmacao == "n" or "N":
            break

    elif opcao == 2:
        nome_do_produto = str(input('Digite o nome do pruduto: '))
        cod_do_produto = str(input('digite o codigo do produto: '))
        custo_do_produto = float(input('digite o custo do produto: : '))
        custo_fixo = int(input('digite o custo fixo do produto: '))
        comissao_de_venda = int(input('qual a comissão de venda'))
        imposto_sobre_venda = int(input('digite o imposto sobre venda: '))
        confirmacao = str(input("produto cadastrado. deseja voltar para o menu? S/N: "))
        if confirmacao == "s" or "S":
            continue
        elif confirmacao == "n" or "N":
            break
    elif opcao == 3:
        print(f"Nome do produto: {nome_do_produto}\nCodigo do produto: {cod_do_produto}")
        confirmacao = str(input("deseja voltar para o menu? S/N: "))
        if confirmacao == "s" or "S":
            continue
        elif confirmacao == "n" or "N":
            break
