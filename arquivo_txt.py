def salvar_txt(nome, patrimonio, valor):
    arquivo = open("equipamentos.txt", "a")
    arquivo.write(nome + " " + patrimonio + " " + valor + "\n")
    arquivo.close()


def ver_historico():
    registros = []
    try:
        arquivo = open("equipamentos.txt", "r")
        linhas = arquivo.readlines()
        arquivo.close()
    except:
        print("Nenhum registro encontrado.")
        return

    for linha in linhas:
        if linha.strip() == "":
            continue
        partes = linha.strip().rsplit(" ", 2)
        nome = partes[0]
        patrimonio = partes[1]
        valor = int(partes[2])

        registros.append((nome, patrimonio, valor))

    registros.sort(key=lambda x: x[2], reverse=True)

    print("\nHistórico")
    posicao = 1

    for registro in registros:
        print(posicao, "-", registro[0], "-", registro[1], "-", registro[2])
        posicao += 1

    print("Total de registros: ", len(registros))
