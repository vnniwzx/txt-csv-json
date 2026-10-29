from arquivo_txt import *
from arquivo_csv import *
from arquivo_json import *

def cadastrar_equipamento():
    nome = input("Nome do equipamento: ")
    patrimonio = input("Patrimônio/Ano: ")
    valor = input("Valor/Custo: ")

    while not valor.isdigit():
        print("Digite apenas números inteiros para o valor.")
        valor = input("Valor/Custo: ")

    salvar_txt(nome, patrimonio, valor)
    salvar_csv(nome, patrimonio, valor)
    salvar_json(nome, patrimonio, valor)

    print("Equipamento salvo!")

while True:
    print("\nInventário do laboratório")
    print("1 - Cadastrar equipamento")
    print("2 - Ver histórico de ocorrências")
    print("3 - Listar inventário completo e gerar relatório")
    print("4 - Buscar equipamento detalhado com estado de conservação")
    print("5 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_equipamento()
    elif opcao == "2":
        ver_historico()
    elif opcao == "3":
        listar_inventario()
    elif opcao == "4":
        buscar_equipamento()
    elif opcao == "5":
        print("Encerrando o sistema...")
        break
    else:
        print("Opção inválida!")