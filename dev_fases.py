ARQUIVO = "nomes.txt"

def carregar_nomes():
    try:
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            return f.read().splitlines()
    except FileNotFoundError:
        return []
    
def salvar_nomes(nomes_lista):
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        for nome in nomes_lista:
            f.write(nome + "\n")

def adicionar_nome(nome, nomes_lista):
    if not nome.strip():
        raise ValueError("Nome vazio.")      
    nomes_lista.append(nome.strip())

def buscar_nomes(lista_de_nomes, busca_nome):
    return busca_nome in lista_de_nomes

def lista_nomess(nomes_lista):
    if not nomes_lista:
        print("A lista está vazia.")
        return
    for i, n in enumerate(nomes_lista, 1):
        print(f"{i}. {n}")

def menu():
    print("\n--- Cadastro de Nomes ---")
    print("1. Adicionar nome")
    print("2. Listar nomes")
    print("3. Buscar nomes")
    print("4. Salvar e sair")
    return input("Opção: ")

if __name__ == "__main__":
 
    lista_nomes = carregar_nomes()

    while True:
        opcao = menu()
        if opcao == "1":
            try:
                nome_input = input("Nome: ")
                adicionar_nome(nome_input, lista_nomes)
                print("Adicionado!")
            except ValueError as e:
                print(f"Erro: {e}")

        elif opcao == "2":
            lista_nomess(lista_nomes)

        elif opcao == "3":
            busca = input("Buscar: ")
            achou = buscar_nomes(lista_nomes, busca)
            print("Encontrou!" if achou else "Não encontrou.")

        elif opcao == "4":
            salvar_nomes(lista_nomes)
            print("Nomes salvos com sucesso! Saindo...")
            break
        else:
            print("Opção inválida!")
