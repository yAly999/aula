precos = {
    "arroz": 25.00,
    "feijao": 8.50,
    "macarrao": 4.30,
    "leite": 5.20,
    "cafe": 18.90,
    "acucar": 6.00,
    "oleo": 9.80,
    "sabao": 12.50,
    "carne": 35.00,
    "frango": 22.00,
}


carrinho = []

print("=== Simulador de Carrinho de Compras ===")
print("Produtos disponíveis:")
for produto, preco in precos.items():
    print(f"  - {produto}: R$ {preco:.2f}")
print()
print('Digite o nome de um produto para adicionar ao carrinho.')
print('Digite "sair" quando terminar.\n')


while True:
    entrada = input("Produto: ").strip().lower()

    if entrada == "sair":
        break

    if entrada in precos:
        carrinho.append(entrada)
        print(f'"{entrada}" adicionado ao carrinho!\n')
    else:
        print(f'Produto "{entrada}" não encontrado na tabela de preços. Tente novamente.\n')


total = 0.0
for item in carrinho:
    total += precos[item]

print("\n=== Resumo da Compra ===")
if carrinho:
    for item in carrinho:
        print(f"  - {item}: R$ {precos[item]:.2f}")
else:
    print("  (carrinho vazio)")

print(f"\nTotal antes do desconto: R$ {total:.2f}")


if total > 100:
    desconto = total * 0.10
    total_final = total - desconto
    print(f"Desconto aplicado (10%): -R$ {desconto:.2f}")
else:
    total_final = total
    print("Sem desconto (total não passou de R$ 100,00).")

print(f"\nValor final a pagar: R$ {total_final:.2f}")