#uma empresa de logistica gerencia enviados e recebidos em seu centro de distribuiçao.Cada pacote tem um codigo de rastreamento e um status entrega. O sistema da empresa armazena esses informaçoes em tuplas imutaveis para evitar alterações indevidas nos registros.
#pacotes =( ("ABC123", "enviado"), ("XYZ789", "recebido"), ("DEF456", "entransito"), ("JKL321", "enviado"), ("MNO654", "recebido"), ("PQR987", "entransito"), ("STU741", enviado"),)
#a empresa precisa implementar um programa que: 1. Conte quantos pacotes estão em cada status: "enviado", "recebido", "entransito". 2. Liste apenas o codigo dos pacotes com status " em transito" 3. Use uma funçao que recebe um codigo de rastreamento e retorne o status do pacote, ou uma mensagem informando que o pacote não esta cadastrado. 4. Ordene os pacotes pelo codigo de rastreamento e exiba a tupla ordenada. Desenvolva um programa em Python que execute essas operaçoes e exiba os resultados o metodo de implementaçao.

pacotes = (("ABC123", "Enviado"), ("XYZ789", "Recebido"), ("DEF456", "Entransito"), ("JKL321", "Enviado"), ("MNO654", "Recebido"), ("PQR987", "Entransito"), ("STU741", "Enviado"))

enviados=0
recebidos=0
em_transito=0

rastreamento=input(" Insira o código de rastreamento")

for código, status in pacotes:
    if status == "Enviado":
        enviados+= 1
    elif status == "Recebido":
        recebidos +=1
    elif status == "em_transito":
        em_transito += 1

print (f"Enviados: {enviados}")
print (f"Recebidos: {recebidos}")
print (f"Em transito: {em_transito}")

for codigo, status in pacotes:
    if status == "em_transito":
        print(codigo)

