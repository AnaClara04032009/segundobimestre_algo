def calculadora_imc (pessoa):
    imc=pessoa ["peso"]/ (pessoa ["altura"] * pessoa ["altura"])
    resultado= f"O IMC {pessoa} é {imc:.2f}"
    #comando ternário:
    saudavel= 18.5 < imc < 25

    return{
        "nome": pessoa ["nome"],
        "imc": imc,
        "resultado": resultado,
        "saudavel": saudavel
    }
pessoa1={
    "nome": "José",
    "peso": 110,
    "altura": 1.75
}
print (calculadora_imc(pessoa1))