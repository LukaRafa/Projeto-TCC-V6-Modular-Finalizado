from materiais import exibir_menu, selecionar_materiais
from planilha import criar_planilha

def main():
    # Perguntar ao técnico se é instalação ou reparo
    tipo_servico = input("O serviço é uma instalação (1) ou reparo (2)? ")

    # Solicitar informações do cliente
    nome_cliente = input("Nome do cliente: ")
    cpf_cliente = input("CPF: ")

    # Perguntar ao técnico quantas horas de trabalho serão necessárias
    horas_trabalho = float(input("Quantas horas de trabalho serão necessárias? "))

    # Perguntar ao técnico qual o valor em R$ para cada hora de trabalho
    valor_hora = float(input("Qual o valor em R$ para cada hora de trabalho? "))

    materiais_selecionados = {}

    while True:
        print("\nCategorias de materiais elétricos:")
        print("1. QDC")
        print("2. Insumos")
        print("3. Aterramento")
        print("4. Rede Aparente")
        print("5. Finalizar")

        escolha_categoria = input("Digite o número da categoria desejada: ")

        if escolha_categoria == '1':
            # Código para categoria QDC (mantido igual)
            qdc = ["Quadro de distribuição",
                "Disjuntor monopolar 10A",
                "Disjuntor monopolar 16A",
                "Disjuntor monopolar 20A",
                "Disjuntor monopolar 25A",
                "Disjuntor monopolar 32A",
                "Disjuntor monopolar 40A",
                "Disjuntor monopolar 50A",
                "Disjuntor monopolar 63A",
                "Disjuntor bipolar 10A",
                "Disjuntor bipolar 20A",
                "Disjuntor bipolar 25A",
                "Disjuntor bipolar 32A",
                "Disjuntor bipolar 40A",
                "Disjuntor bipolar 50A",
                "Disjuntor bipolar 63A",
                "Disjuntor tripolar 10A",
                "Disjuntor tripolar 20A",
                "Disjuntor tripolar 25A",
                "Disjuntor tripolar 32A",
                "Disjuntor tripolar 40A",
                "Disjuntor tripolar 50A",
                "Disjuntor tripolar 63A",
                "DPS 175/20KA",
                "DPS 175V/45KA",
                "DPS 275/20KA",
                "DPS 275V/45KA",
                "IDR 20A 30mA - 2 POLOS",
                "IDR 40A 30mA - 2 POLOS",
                "IDR 63A 30mA - 2 POLOS",
                "IDR 80A 30mA - 2 POLOS",
                "IDR 20A 30mA - 4 POLOS",
                "IDR 40A 30mA - 4 POLOS",
                "IDR 63A 30mA - 4 POLOS",
                "IDR 80A 30mA - 4 POLOS",
                "Barramento tipo pente 80A monopolar",
                "Barramento tipo pente 80A bipolar",
                "Barramento tipo pente 80A tripolar"
                # ... (Lista de materiais QDC)
            ]
            selecionar_materiais('QDC', qdc, materiais_selecionados)
        elif escolha_categoria == '2':
            # Código para categoria Insumos (mantido igual)
            insumos = ["Caixa de passagem de embutir 2\"x4\"",
                "Caixa de passagem de embutir 4\"x4\"",
                "Caixa de passagem de embutir 20x20",
                "Caixa de passagem de embutir 30x30",
                "Caixa de passagem de embutir 40x40",
                "Caixa octogonal 3\"x3\"",
                "Caixa octogonal 4\"x4\"",
                "Paflon Bocal E27",
                "Lâmpada Bocal E27",
                "Modulo tomada 2P+T 10A",
                "Modulo tomada 2P+T 20A",
                "Modulo Passa Fio",
                "Modulo interruptor simples",
                "Modulo interruptor paralelo",
                "Placa 4x2\" para 1 módulo horizontal  + suporte",
                "Placa 4x4\" para 4 módulos horizontais  + suporte",
                "Placa 4x2\" para 2 módulos horizontais  + suporte",
                "Placa 4x4\" para 2 módulos horizontais  + suporte",
                "Placa 4x2\" para 3 módulos horizontais  + suporte",
                "Placa 4x2\" cega + suporte",
                "Placa 4x4\" cega  + suporte",
                "Conector pino curto ( vulgo conector genérico )",
                "Conector tubular 1,5mm2",
                "Conector tubular 2,5mm2",
                "Conector tubular 4,0mm2",
                "Conector tubular 6,0mm2",
                "Conector tubular 10,0mm2",
                "Anilha para cabos até 6,0mm2 - numero 0",
                "Anilha para cabos até 6,0mm2 - numero 1",
                "Anilha para cabos até 6,0mm2 - numero 2",
                "Anilha para cabos até 6,0mm2 - numero 3",
                "Anilha para cabos até 6,0mm2 - numero 4",
                "Anilha para cabos até 6,0mm2 - numero 5",
                "Anilha para cabos até 6,0mm2 - numero 6",
                "Anilha para cabos até 6,0mm2 - numero 7",
                "Anilha para cabos até 6,0mm2 - numero 8",
                "Anilha para cabos até 6,0mm2 - numero 9",
                "Anilha para cabos 16,0mm2 - letra R",
                "Anilha para cabos 16,0mm2 - letra S",
                "Anilha para cabos 16,0mm2 - letra T",
                "Anilha para cabos 16,0mm2 - letra N",
                "Abraçadeiras hellermann T18L",
                "Eletroduto flexivel corrugado 3/4\"",
                "Eletroduto flexivel corrugado 1\"",
                "Eletroduto flexivel corrugado 1 1/2\"",
                "Eletroduto flexivel corrugado 2\"",
                "Conector WAGO 2 vias",
                "Conector WAGO 3 vias",
                "Conector WAGO 5 vias",
                "Fita isolante alta fusão",
                "Fita isolante tipo C",
                "Fita isolante tipo B",
                "Grampo para haste de aterramento",
                "Caixa de inspeção PVC 300mm x 250mm",
                "Tampa para caixa de inspeção 300mm",
                "Haste aterramento cobreada 2,4m",
                "Terminal de compressão 16mm2",
                "Cobre nu 50mm2"
                # ... (Lista de materiais Insumos)
            ]
            selecionar_materiais('Insumos', insumos, materiais_selecionados)
        elif escolha_categoria == '3':
            # Código para categoria Aterramento (mantido igual)
            aterramento = ["Grampo para haste de aterramento",
                            "Caixa de inspeção PVC 300mm x 250mm",
                            "Tampa para caixa de inspeção 300mm",
                            "Haste aterramento cobreada 2,4m",
                            "Terminal de compressão 16mm2",
                            "Cobre nu 50mm2"
                # ... (Lista de materiais Aterramento)
            ]
            selecionar_materiais('Aterramento', aterramento, materiais_selecionados)
        elif escolha_categoria == '4':
            # Código para categoria Rede Aparente (mantido igual)
            rede_aparente = ["Eletroduto galvanizado 3/4\" - Barra 3m",
                "Eletroduto galvanizado 1\" - Barra 3m",
                "Condulete galvanizado 5 entradas - 3/4\"",
                "Condulete galvanizado 5 entradas - 1\"",
                "Tampão Para Condulete 3/4\"",
                "Tampão Para Condulete 1\"",
                "Unidut conico 3/4\"",
                "Unidut conico 1\"",
                "Unidut Reto 3/4\"",
                "Unidut Reto 1\"",
                "Abraçadeira Tipo \"D\" Com Cunha 3/4\"",
                "Abraçadeira Tipo \"D\" Com Cunha 1\"",
                "Bucha para condulete 3/4\"",
                "Arruela para condulete 3/4\"",
                "Bucha para condulete 1\"",
                "Arruela para condulete 1\"",
                "Curva galvanizada 90º 3/4\"",
                "Curva galvanizada 90º 1\"",
                "Tampa para Condulete 3/4\" para 1 modulo Horizontal",
                "Tampa para condulete 3/4\" para 2 modulos horizontais",
                "Tampa para Condulete 1\" para 1 modulo Horizontal",
                "Tampa para condulete 1\" para 2 modulos horizontais",
                "Parafusos sextavado rosca soberba 8mm x 50mm",
                "Bucha plástica para bloco 8mm"
                # ... (Lista de materiais Rede Aparente)
            ]
            selecionar_materiais('Rede Aparente', rede_aparente, materiais_selecionados)
        elif escolha_categoria == '5':
            break
        else:
            print("Opção inválida. Tente novamente.")

    # Criar a planilha com os materiais selecionados
    criar_planilha(nome_cliente, tipo_servico, cpf_cliente, materiais_selecionados, horas_trabalho, valor_hora)

    # Adicione esta seção ao final do script para imprimir as seleções
    print("\nResumo das seleções:")
    for material, quantidade in materiais_selecionados.items():
        print(f"{quantidade} unidades de {material}")

if __name__ == "__main__":
    main()
