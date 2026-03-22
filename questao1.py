def main():
    lista_funcionarios = []
    resp = 1

    while (resp == 1):
        print("\n1 - Inserir funcionario")
        print("2 - Alterar funcionario")
        print("3 - Excluir funcionario")
        print("4 - Exibir dados de um funcionario")
        print("5 - Exibir funcionarios nascidos a partir de 1989 com salario liquido entre 8000 e 15000")
        print("7 - Exibir Cientistas de Dados com salario bruto maior que 14000")
        opc = int(input("Digite a opcao desejada: "))

        if (opc == 1):
            inserir_funcionario(lista_funcionarios)
        elif (opc == 2):
            codigo_alterar = int(input("Digite o codigo do funcionario que deseja alterar: "))
            indice = buscar_funcionario(lista_funcionarios, codigo_alterar)
            if (indice != -1):
                alterar_funcionario(lista_funcionarios, indice)
            else:
                print("Codigo inexistente!")
        elif (opc == 3):
            codigo_excluir = int(input("Digite o codigo do funcionario que deseja excluir: "))
            indice = buscar_funcionario(lista_funcionarios, codigo_excluir)
            if (indice != -1):
                excluir_funcionario(lista_funcionarios, indice)
            else:
                print("Codigo inexistente!")
        elif (opc == 4):
            codigo_exibir = int(input("Digite o codigo do funcionario que deseja exibir: "))
            indice = buscar_funcionario(lista_funcionarios, codigo_exibir)
            if (indice != -1):
                exibir_funcionario(lista_funcionarios, indice)
            else:
                print("Codigo inexistente!")
        elif (opc == 5):
            relatorio_aniversariantes(lista_funcionarios)
        elif (opc == 7):
            relatorio_cientistas(lista_funcionarios)
        else:
            print("Opcao invalida!")

        resp = int(input("\nDeseja continuar (1-SIM/0-NAO)? "))


def buscar_funcionario(lista_funcionarios, codigo):
    indice = -1
    for i in range(len(lista_funcionarios)):
        if (lista_funcionarios[i]['Codigo'] == codigo):
            indice = i
    return (indice)


def inserir_funcionario(lista_funcionarios):
    try:
        codigo = int(input("Codigo: "))
        indice = buscar_funcionario(lista_funcionarios, codigo)
        while (indice != -1):
            codigo = int(input("Codigo ja existente. Digite outro codigo: "))
            indice = buscar_funcionario(lista_funcionarios, codigo)
        nome = input("Nome: ")
        cpf = input("CPF: ")
        dia = int(input("Dia de nascimento: "))
        mes = int(input("Mes de nascimento: "))
        ano = int(input("Ano de nascimento: "))
        data_nascimento = [dia, mes, ano]
        cargo = input("Cargo: ")
        salario_bruto = float(input("Salario bruto: "))
    except ValueError:
        print("Digite valores numericos onde necessario!")
    else:
        desconto_inss = salario_bruto * 0.15
        desconto_ir = salario_bruto * 0.1895
        salario_liquido = salario_bruto - desconto_inss - desconto_ir

        dados_funcionario = {
            'Codigo': codigo,
            'Nome': nome,
            'CPF': cpf,
            'Data_nascimento': data_nascimento,
            'Cargo': cargo,
            'Salario_bruto': salario_bruto,
            'Desconto_INSS': desconto_inss,
            'Desconto_IR': desconto_ir,
            'Salario_liquido': salario_liquido
        }
        lista_funcionarios.append(dados_funcionario)
        print("Funcionario inserido com sucesso!")


def alterar_funcionario(lista_funcionarios, indice):
    try:
        print(f"Nome: {lista_funcionarios[indice]['Nome']}")
        novo_nome = input("Novo nome: ")
        print(f"CPF: {lista_funcionarios[indice]['CPF']}")
        novo_cpf = input("Novo CPF: ")
        print(f"Data de nascimento: {lista_funcionarios[indice]['Data_nascimento']}")
        dia = int(input("Novo dia de nascimento: "))
        mes = int(input("Novo mes de nascimento: "))
        ano = int(input("Novo ano de nascimento: "))
        nova_data = [dia, mes, ano]
        print(f"Cargo: {lista_funcionarios[indice]['Cargo']}")
        novo_cargo = input("Novo cargo: ")
        print(f"Salario bruto: {lista_funcionarios[indice]['Salario_bruto']}")
        novo_salario_bruto = float(input("Novo salario bruto: "))
    except ValueError:
        print("Digite valores numericos onde necessario!")
    else:
        novo_desconto_inss = novo_salario_bruto * 0.15
        novo_desconto_ir = novo_salario_bruto * 0.1895
        novo_salario_liquido = novo_salario_bruto - novo_desconto_inss - novo_desconto_ir

        lista_funcionarios[indice]['Nome'] = novo_nome
        lista_funcionarios[indice]['CPF'] = novo_cpf
        lista_funcionarios[indice]['Data_nascimento'] = nova_data
        lista_funcionarios[indice]['Cargo'] = novo_cargo
        lista_funcionarios[indice]['Salario_bruto'] = novo_salario_bruto
        lista_funcionarios[indice]['Desconto_INSS'] = novo_desconto_inss
        lista_funcionarios[indice]['Desconto_IR'] = novo_desconto_ir
        lista_funcionarios[indice]['Salario_liquido'] = novo_salario_liquido
        print("Dados alterados com sucesso!")


def excluir_funcionario(lista_funcionarios, indice):
    lista_funcionarios.pop(indice)
    print("Funcionario excluido com sucesso!")


def exibir_funcionario(lista_funcionarios, indice):
    for chave, valor in lista_funcionarios[indice].items():
        print(f"{chave}: {valor}")


def relatorio_aniversariantes(lista_funcionarios):
    print("\n*** Funcionarios nascidos a partir de 1989 com salario liquido entre 8000 e 15000 ***")
    encontrou = False
    for i in range(len(lista_funcionarios)):
        ano_nasc = lista_funcionarios[i]['Data_nascimento'][2]
        sal_liq = lista_funcionarios[i]['Salario_liquido']
        if (ano_nasc >= 1989 and sal_liq >= 8000.00 and sal_liq <= 15000.00):
            for chave, valor in lista_funcionarios[i].items():
                print(f"{chave}: {valor}")
            print("-------------------------------------------")
            encontrou = True
    if (not encontrou):
        print("Nenhum funcionario encontrado com esses criterios.")


def relatorio_cientistas(lista_funcionarios):
    print("\n*** Cientistas de Dados com salario bruto maior que 14000 ***")
    encontrou = False
    for i in range(len(lista_funcionarios)):
        if (lista_funcionarios[i]['Cargo'] == "Cientista de Dados" and lista_funcionarios[i]['Salario_bruto'] > 14000.00):
            for chave, valor in lista_funcionarios[i].items():
                print(f"{chave}: {valor}")
            print("-------------------------------------------")
            encontrou = True
    if (not encontrou):
        print("Nenhum funcionario encontrado com esses criterios.")


if (__name__ == "__main__"):
    main()
