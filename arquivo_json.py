import json

def carregar_dados():
    try:
        with open("equipamentos.json", "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    except:
        return []

def salvar_dados(equipamentos):
    with open("equipamentos.json", "w", encoding="utf-8") as arquivo:
        json.dump(equipamentos, arquivo, indent=4, ensure_ascii=False)

def salvar_json(nome, patrimonio, valor):
    equipamentos = carregar_dados()

    equipamento = {
        "nome": nome,
        "patrimonio": patrimonio,
        "valor": int(valor)
    }
    equipamentos.append(equipamento)
    salvar_dados(equipamentos)

def definir_nivel(valor):
    if valor < 50:
        return "Necessita Substituição"
    elif valor < 80:
        return "Regular"
    else:
        return "Excelente Estado"

def buscar_equipamento():
    nome_busca = input("Digite o nome do equipamento: ")

    equipamentos = carregar_dados()
    encontrado = False

    for equipamento in equipamentos:
        nome = equipamento.get("nome", equipamento.get("nome do equipamento", ""))
        patrimonio = equipamento.get("patrimonio", equipamento.get("patrimônio", ""))
        valor = int(equipamento.get("valor", 0))

        if nome.lower() == nome_busca.lower():
            print("\n=== EQUIPAMENTO ENCONTRADO ===")
            print("Nome:", nome)
            print("Patrimônio:",patrimonio)
            print("Valor:", valor)
            print("Estado de Conservação:", definir_nivel(valor))
            encontrado = True

    if not encontrado:
        print("Equipamento não encontrado.")