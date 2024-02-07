import openpyxl

def exibir_menu(categoria, lista_materiais):
    print(f"\nSelecione o material {categoria}:")
    for i, material in enumerate(lista_materiais, start=1):
        print(f"{i}. {material}")
    print("0. Voltar")

def selecionar_quantidade():
    while True:
        try:
            quantidade = float(input("Digite a quantidade desejada: "))
            if quantidade < 0:
                raise ValueError("A quantidade não pode ser negativa.")
            return quantidade
        except ValueError as e:
            print(f"Erro: {e}. Tente novamente.")

def selecionar_materiais(categoria, lista_materiais, materiais_selecionados):
    while True:
        exibir_menu(categoria, lista_materiais)
        escolha_material = input("Digite o número do material desejado: ")

        if escolha_material == '0':
            break

        try:
            indice_material = int(escolha_material) - 1
            material_selecionado = lista_materiais[indice_material]

            if categoria == 'Cabos':
                quantidade = selecionar_quantidade()
                materiais_selecionados[material_selecionado] = quantidade
            else:
                quantidade = int(input("Digite a quantidade desejada: "))
                materiais_selecionados[material_selecionado] = quantidade

            print(f"{quantidade} unidades de {material_selecionado} adicionadas.")
        except (ValueError, IndexError):
            print("Opção inválida. Tente novamente.")
