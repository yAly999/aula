# while True:
#     senha = input("Qual é a senha: ")

#     if senha == '123':
#         print("Acesso liberado!")
#         break
#     else:
#         print("Acesso negado, tente novamente")    

estoque = {"caneta": 10, "lapis": 5, "boracha": 0}

for item, qtd in estoque.items():
    if qtd == 0:
        print(f"{item}: esgotado")
    else:
        print(f"{item}: {qtd}")    