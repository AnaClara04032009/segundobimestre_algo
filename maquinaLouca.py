import time

#variaveisglobais
ligado = False
tempo = 0
potencia = 0
 
def ligar(novo_tempo, nova_potencia):
    global ligado, tempo, potencia
    if not ligado:
        ligado = True
        tempo = novo_tempo
        potencia = nova_potencia
        print(f'maquinalouca ligada por {tempo} segundos na potencia {potencia}')
        iniciar_cronometro(tempo)
        desligar() #desligar automatcamente
    else:
        print('maquinaLouca ja esta ligada')

def desligar():
    global ligado
    if ligado:
         ligado = False
         print('maquinalouca desligada')
    else:
         print('maquinaLouca ja esta desligada')

def status():
     if ligado:
        print(f' tempo:{tempo} segundos /n potencia: {potencia}')
     else:
        print(f"desligado")

def iniciar_cronometro(segundos):
    while segundos>0:
        print(f"tempo restante: {segundos} segundos" , end="\r")
        time.sleep(1)
        segundos -= 1  #segundos = segundos - 1
        print ("\n tempo esgotado")

def vidro():
         ligar(120, 100)
def plastico():
         ligar(60,21)
def metal():
         ligar(120, 30)



opcao = int(input('escolha oque deseja lavar: \n 1 - vidro \n 2 - plastico' '\n 3 - metal \n'))
if opcao == 1:
    vidro()
elif opcao == 2:
    plastico()
elif opcao == 3:
    metal()
else:
    print('opcao invalida')