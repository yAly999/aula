oficina_geral = []

def cadastrar_ordem_servico():
    print("\n--- NOVA ORDEM DE SERVIÇO ---")

    cliente = input("Nome do cliente: ")
    modelo_carro = input("Modelo do veículo: ")

    while True:
        try:
            ano_carro = int(input("Ano do carro (AAAA): "))
            if ano_carro < 1900 or ano_carro > 2026:
                print("Erro: Digite um ano válido.")
                continue
            break
        except ValueError:
            print("ERRO: O ano deve ser um número inteiro!")

    while True:
        try:
            quilometragem = int(input("Quilometragem do carro: "))
            if quilometragem < 0:
                print("A quilometragem não pode ser negativa!")
                continue
            break
        except ValueError:
            print("ERRO: A quilometragem deve ser um número inteiro!")

    necessita_revisao_completa = False

    if quilometragem > 10000 or ano_carro < 2020:
        print("\nAlerta do sistema: O carro necessita de revisão preventiva.")        
        necessita_revisao_completa = True
    else:
        print("\nStatus: Manutenção de rotina.")

    lista_pecas = []
    total_orcamento = 0.00

    print("\n--- LANÇAMENTO DE PEÇAS E SERVIÇOS ---")

    while True:
        peca = input("Nome de peça/serviço (ou 'fim' para encerrar): ").strip()
        if peca.lower() == 'fim':
            break
        try:
            preco = float(input(f"Preço de '{peca}': R$ "))
            if preco < 0:
                print("O preço não pode ser negativo!")
                continue
            lista_pecas.append(peca)
            total_orcamento += preco
        except ValueError:
            print("ERRO: Preço inválido! Item desconsiderado. Tente novamente.")

    ordem_servico = {
        "cliente": cliente,
        "veiculo": modelo_carro,
        "ano": ano_carro,
        "km": quilometragem,
        "alerta_revisao": necessita_revisao_completa,
        "itens": lista_pecas,
        "total": total_orcamento,
        "status": "Em aberto"
    }        

    oficina_geral.append(ordem_servico)
    print(f"\nOrdem de serviço de {cliente} gerada com sucesso!")

def lista_todas_as_ordens():
    print("\n" + 30 * "=")
    print(" RELATÓRIO GERAL DA OFICINA")
    print(30 * "=")

    if not oficina_geral:
        print("Nenhum veículo em manutenção no momento.")
        return
    
    for indice, ordem in enumerate(oficina_geral, 1):
        print(f"\n#OS: {indice} | Cliente: {ordem['cliente']} | Carro: {ordem['veiculo']}")
        print(f"Ano: {ordem['ano']} | KM: {ordem['km']} | Total: R$ {ordem['total']:.2f}")
        print(f"Revisão crítica: {'SIM' if ordem['alerta_revisao'] else 'NÃO'}")
        print(f"Itens trocados: {', '.join(ordem['itens']) if ordem['itens'] else 'Nenhum item lançado'}")
        print(f"Total: R$ {ordem['total']:.2f}")
        print(f"Status: {ordem['status']}")
        print(f"-" *45)

while True:
    print("\n=== SISTEMA INTELIGENTE ===")        
    print("1. Cadastrar nova ordem de serviço")
    print("2. listar ordem de serviço relatorio")
    print("3. sair do sistema")

    opcao = input("Escolher uma opção")

    if opcao == "1":
        cadastrar_ordem_servico()

    elif opcao == "2":
        lista_todas_as_ordens()

    elif opcao == "3":
        print("Fecha o sistema. Até logo, meu caro!")
        break

    else:
        print("opcao invalida!! tente novamente")

        
                        


