import csv

def salvar_csv(nome, patrimonio, valor):
    with open("equipamentos.csv", "a", newline="") as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow([nome, patrimonio, valor])

def listar_inventario():
    equipamentos = []
    try:
        with open("equipamentos.csv", "r") as arquivo:
            leitor = csv.reader(arquivo)

            print("\nInventário")

            for linha in leitor:
                nome = linha[0]
                patrimonio = linha[1]
                valor = int(linha[2])

                print(f"{nome} - {patrimonio} - {valor}")
                equipamentos.append([nome, patrimonio, valor])
    except:
        print("Nenhum equipamento cadastrado.")
        return

    if len(equipamentos) == 0:
        print("Nenhum equipamento cadastrado.")
        return

    total_valor = 0
    maior_valor = 0
    item_mais_valioso = ""

    for equipamento in equipamentos:
        valor = equipamento[2]

        total_valor += valor
        if valor > maior_valor:
            maior_valor = valor
            item_mais_valioso = equipamento[0]
    media = total_valor / len(equipamentos)

    print("\nRelatório")
    print(f"Total de equipamentos: {len(equipamentos)}")
    print(f"Média de valor: {media:.2f}")
    print(f"Item mais valioso: {item_mais_valioso}")
    print(f"Maior valor: {maior_valor}")
