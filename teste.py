print('#'*20)
print('menu de opçoes')
print('#'*20)
opcao = int(input('[1] para cadastrar um novo produto\n[2] para alterar os dados de algum produto\n[3] para listar os produtos'))
if opcao == 1:
    nome_do_produto = str(input('Digite o nome do pruduto: '))
    cod_do_produto = str(input('digite o codigo do produto: '))
    preco_de_venda = str(input('digite o preço de venda do produto:'))
    custo_do_produto = str(input('digite o custo do produto: : '))
    custo_fixo = str(input('digite o custo fixo do produto: '))
    comissao_de_venda = str(input('qual a comissão de venda'))
    imposto_sobre_venda = str(input('digite o imposto sobre venda: '))

elif opcao == 2:
    nome_do_produto = str(input('Digite o nome do pruduto: '))
elif opcao
