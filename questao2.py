def main():
    lista_medicamentos = []
    resp = 1

    while (resp == 1):
        print("\n1 - Inserir medicamento")
        print("2 - Alterar medicamento")
        print("3 - Excluir medicamento")
        print("4 - Exibir dados de um medicamento")
        print("5 - Exibir medicamentos com ano de validade superior a 2025")
        print("7 - Exibir medicamentos com valor de compra entre 120.00 e 450.00")
        opc = int(input("Digite a opcao desejada: "))

        if (opc == 1):
            inserir_medicamento(lista_medicamentos)
        elif (opc == 2):
            codigo_alterar = int(input("Digite o codigo do medicamento que deseja alterar: "))
            indice = buscar_medicamento(lista_medicamentos, codigo_alterar)
            if (indice != -1):
                alterar_medicamento(lista_medicamentos, indice)
            else:
                print("Codigo inexistente!")
        elif (opc == 3):
            codigo_excluir = int(input("Digite o codigo do medicamento que deseja excluir: "))
            indice = buscar_medicamento(lista_medicamentos, codigo_excluir)
            if (indice != -1):
                excluir_medicamento(lista_medicamentos, indice)
            else:
                print("Codigo inexistente!")
        elif (opc == 4):
            codigo_exibir = int(input("Digite o codigo do medicamento que deseja exibir: "))
            indice = buscar_medicamento(lista_medicamentos, codigo_exibir)
            if (indice != -1):
                exibir_medicamento(lista_medicamentos, indice)
            else:
                print("Codigo inexistente!")
        elif (opc == 5):
            relatorio_validade(lista_medicamentos)
        elif (opc == 7):
            relatorio_valor_compra(lista_medicamentos)
        else:
            print("Opcao invalida!")

        resp = int(input("\nDeseja continuar (1-SIM/0-NAO)? "))


def buscar_medicamento(lista_medicamentos, codigo):
    indice = -1
    for i in range(len(lista_medicamentos)):
        if (lista_medicamentos[i]['Codigo'] == codigo):
            indice = i
    return (indice)


def inserir_medicamento(lista_medicamentos):
    try:
        codigo = int(input("Codigo do medicamento: "))
        indice = buscar_medicamento(lista_medicamentos, codigo)
        while (indice != -1):
            codigo = int(input("Codigo ja existente. Digite outro codigo: "))
            indice = buscar_medicamento(lista_medicamentos, codigo)
        descricao = input("Descricao do medicamento: ")
        dia = int(input("Dia de validade: "))
        mes = int(input("Mes de validade: "))
        ano = int(input("Ano de validade: "))
        data_validade = [dia, mes, ano]
        valor_compra = float(input("Valor de compra: "))
    except ValueError:
        print("Digite valores numericos onde necessario!")
    else:
        valor_venda = valor_compra * 1.30

        dados_medicamento = {
            'Codigo': codigo,
            'Descricao': descricao,
            'Data_validade': data_validade,
            'Valor_compra': valor_compra,
            'Valor_venda': valor_venda
        }
        lista_medicamentos.append(dados_medicamento)
        print("Medicamento inserido com sucesso!")
    finally:
        print("Operacao de insercao finalizada.")


def alterar_medicamento(lista_medicamentos, indice):
    try:
        print(f"Descricao: {lista_medicamentos[indice]['Descricao']}")
        nova_descricao = input("Nova descricao: ")
        print(f"Data de validade: {lista_medicamentos[indice]['Data_validade']}")
        dia = int(input("Novo dia de validade: "))
        mes = int(input("Novo mes de validade: "))
        ano = int(input("Novo ano de validade: "))
        nova_data = [dia, mes, ano]
        print(f"Valor de compra: {lista_medicamentos[indice]['Valor_compra']}")
        novo_valor_compra = float(input("Novo valor de compra: "))
    except ValueError:
        print("Digite valores numericos onde necessario!")
    else:
        novo_valor_venda = novo_valor_compra * 1.30

        lista_medicamentos[indice]['Descricao'] = nova_descricao
        lista_medicamentos[indice]['Data_validade'] = nova_data
        lista_medicamentos[indice]['Valor_compra'] = novo_valor_compra
        lista_medicamentos[indice]['Valor_venda'] = novo_valor_venda
        print("Dados alterados com sucesso!")
    finally:
        print("Operacao de alteracao finalizada.")


def excluir_medicamento(lista_medicamentos, indice):
    lista_medicamentos.pop(indice)
    print("Medicamento excluido com sucesso!")


def exibir_medicamento(lista_medicamentos, indice):
    for chave, valor in lista_medicamentos[indice].items():
        print(f"{chave}: {valor}")


def relatorio_validade(lista_medicamentos):
    print("\n*** Medicamentos com ano de validade superior a 2025 ***")
    encontrou = False
    for i in range(len(lista_medicamentos)):
        ano_validade = lista_medicamentos[i]['Data_validade'][2]
        if (ano_validade > 2025):
            for chave, valor in lista_medicamentos[i].items():
                print(f"{chave}: {valor}")
            print("-------------------------------------------")
            encontrou = True
    if (not encontrou):
        print("Nenhum medicamento encontrado com esse criterio.")


def relatorio_valor_compra(lista_medicamentos):
    print("\n*** Medicamentos com valor de compra entre 120.00 e 450.00 ***")
    encontrou = False
    for i in range(len(lista_medicamentos)):
        val_compra = lista_medicamentos[i]['Valor_compra']
        if (val_compra >= 120.00 and val_compra <= 450.00):
            for chave, valor in lista_medicamentos[i].items():
                print(f"{chave}: {valor}")
            print("-------------------------------------------")
            encontrou = True
    if (not encontrou):
        print("Nenhum medicamento encontrado com esse criterio.")


if (__name__ == "__main__"):
    main()
