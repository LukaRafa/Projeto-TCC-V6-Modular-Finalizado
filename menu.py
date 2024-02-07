# menu.py

def exibir_menu(categorias):
    print("\nCategorias de materiais elétricos:")
    for i, categoria in enumerate(categorias, start=1):
        print(f"{i}. {categoria}")
    print("0. Finalizar")
    
    escolha_categoria = input("Digite o número da categoria desejada: ")
    return escolha_categoria
