

def cadastrar_funcionario():
    print("="*50)
    print("Cadastro de funcionario")
    print("="*50)


    nome = input("Nome de funcionario: ")
    setor = input("Setor (jurico/marketing/TI/Vendas)")
    salario = float(input("Salario (Ex: 1450.00): R$ "))
    cargo = input("Cargo (gerente/ansalista): ")
    bonus = float(input("Bonus (ex:850.00) R$: "))

    linha = f"{setor}, {nome}, {salario:.2f}, {cargo}, {bonus:.2f} \n"

    print("Funcionario  cadastrado com sucesso!")
    print(f"Dados salvo em 'funcionario.txt")

    with open("funcionarios.txt", "a", encoding="utf-8") as arquivo: arquivo.write(linha)
    return{"setor":setor, "nome":nome, "salario":salario, "cargo":cargo, "bonus":bonus}

novo_funcionario = cadastrar_funcionario()
print ("\n Dados cadastrados: ", novo_funcionario)

def somasse(intervalo_lista, criterio, valor_soma):
    