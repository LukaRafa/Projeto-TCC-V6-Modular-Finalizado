import openpyxl
from babel.numbers import format_currency

def criar_planilha(nome_cliente, tipo_servico, cpf_cliente, materiais_selecionados, horas_trabalho, valor_hora):
    # Criar um objeto de workbook
    wb = openpyxl.Workbook()

    # Adicionar uma planilha
    ws = wb.active
    ws.title = "Orçamento"

    # Adicionar cabeçalho
    cabecalho = ["Tipo de Serviço", "Nome do Cliente", "CPF do Cliente", "Horas de Trabalho", "Preço da Hora"]
    ws.append(cabecalho)

    # Traduzir o tipo de serviço para "instalação" ou "reparo"
    tipo_servico_descricao = "Instalação" if tipo_servico == 1 else "Reparo"

    # Adicionar dados de cliente e serviço à planilha
    ws.append([tipo_servico_descricao, nome_cliente, cpf_cliente, horas_trabalho, format_currency(valor_hora, 'BRL', locale='pt_BR')])

    # Calcular o custo total da mão de obra
    custo_mao_de_obra = horas_trabalho * valor_hora

    # Adicionar informações de mão de obra à planilha
    ws.append(["Mão de Obra", horas_trabalho, format_currency(valor_hora, 'BRL', locale='pt_BR'), format_currency(custo_mao_de_obra, 'BRL', locale='pt_BR')])

    # Adicionar uma linha em branco
    ws.append([])

    # Adicionar cabeçalho para materiais
    cabecalho_materiais = ["Descrição", "Quantidade"]
    ws.append(cabecalho_materiais)

    # Adicionar dados de materiais à planilha
    for material, quantidade in materiais_selecionados.items():
        ws.append([material, quantidade])

    # Salvar a planilha
    nome_arquivo = f"{tipo_servico_descricao}_{nome_cliente}.xlsx"
    wb.save(nome_arquivo)

    print(f"Arquivo '{nome_arquivo}' gerado com sucesso.")
