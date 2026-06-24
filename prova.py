# x = 10
# if x > 5: 
#     print("maior")
# elif x == 10:
#     print("igual")
# else:
#     print("menor")        


# frutas = ["maçã", "banana", "uva"]
# for f in frutas:
#     if f == "banana":
#         print(f.upper())
#     else:
#         print(f[0])        

# aluno = {"nome": "Lucas", "nota":8.5 , "aprovado": True}
# for chave, valor in aluno.items():
#     print(f"{chave}: {valor}")



# try:
#     resultado = 10/ 0
#     print(resultado)
# except ZeroDivisionError:
#     print("Erro: divisão por zero")
# finally:
#     print("Fim do programa")    


# dados = {"id": 1, "status": "ativo"}
# for chave, valor in dados.items():
#     print(chave, valor)


# estoque = {"caneta": 5, "lapis": 0, "borracha": 3}

# item = "lapis"

# if item in estoque and estoque[item] > 0:
#     print("Disponível")
# else:
#     print("Indisponível")        



# valores = [11,12 ,13 ,14 ,15,16]
# for num in valores:
#     if num % 2 == 0:
#         print(num)
  

# usuario = {"nome": "Carlos", "idade": 30}
# usuario["Cargo"] = "engenheiro"  
# print(usuario)

while True:
    resposta= input("Digite algo: ")

    if  resposta == "sair":
        break