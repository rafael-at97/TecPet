import time
import os
import RPi.GPIO as GPIO
import numpy as np

# Definição dos pinos das boias (Boia_1 superior e Boia_2 inferior)
Boia_1 = 
Boia_2 = 

# Portas da leitura da balança
ADDO =     # Input Data
ADSK =     # Clock

# Conexões da primeira bobina do motor de passo
IN1 = 
IN2 = 
# Conexões da segunda bobina do motor de passo
IN3 = 
IN4 = 

# Tabela de sequência para os passos do motor
sequence = np.array([[1,0,0,1], [0,1,0,1], [0,1,1,0], [1,0,1,0]])

def gpio_setup():
    # Definição de modo da biblioteca RPi.GPIO:
    # GPIO.BOARD = Número dos pinos no esquemático da placa
    # GPIO.BCM   = Número de "Broadcom SOC Channel", escritos depois de "GPIO" no esquemático da placa
    GPIO.setmode(GPIO.BCM)
    
    # Definição das boias como normalmente abertas
    GPIO.setup(Boia_1, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
    GPIO.setup(Boia_2, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
    
    # Definição das portas da balança
    GPIO.setup(ADDO, GPIO.IN, pull_up_down = GPIO.PUD_UP)    # Entrada para receber os dados
    GPIO.setup(ADSK, GPIO.OUT) # Saída para o clock
    
    # Portas do motor como saída
    GPIO.setup(IN1, GPIO.OUT)
    GPIO.setup(IN2, GPIO.OUT)
    GPIO.setup(IN3, GPIO.OUT)
    GPIO.setup(IN4, GPIO.OUT)
    
def rotate(state, steps):
    for i in range(0, abs(steps)):
        state = (state + steps/abs(steps) + 4)%4
        GPIO.output(IN1, sequence[state, 0])
        GPIO.output(IN2, sequence[state, 1])
        GPIO.output(IN3, sequence[state, 2])
        GPIO.output(IN4, sequence[state, 3])
    time.sleep(tempo)
      
    return state    
    
# Função para leitura efetiva do módulo ADC da balança
def ReadCount():
	  Count = 0
	  
	  # Seguindo o datasheet do ADC, definir o clock inicial como 0
	  GPIO.output(ADSK, False)
	  
	  # De acordo com o datasheet, enquanto a saida de ADDO for 1, a conversao ainda nao esta pronto
	  while GPIO.input(ADDO):
	 
	  # Quando a saída estiver pronta, mandar o sinal de clock, um pulso por vez, e esperar a resposta em bits, MSB primeiro
	  for i in range (0, 24):
		    GPIO.output(ADSK, True)
		    # Cuidado pois as manipulacoes de bit no python podem mudar de versão pra versão
		    Count = Count << 1
		    if GPIO.input(ADDO) == True :
			      Count += 1
        GPIO.output(ADSK, False)
  
  	GPIO.output(ADSK, True)
	  Count = Count^0x800000
	  GPIO.output(ADSK, False)
  
    return Count    

def boias():
    boia_1 = GPIO.input(Boia_1)
    boia_2 = GPIO.input(Boia_2)
    if boia_1 and boia_2:
        # Tanque cheio, definir rotina:
    elif not boia_1 and boia_2:
        # Tanque pela "metade", definir rotina:
    elif boia_1 and not boia_2:
        # Erro nas leituras das boias:
    else:
        # Nível de água abaixo da boia inferior, "vazio", definir rotina:    
    time.sleep(0.1)
  
def main():
    gpio_setup()
    state = 0
    
    while True:
        # Rotina das boias
        boias()
        
        # Leitura da balança
        convert = ReadCount()
        print(convert)
        time.sleep(2000)
        
        # Rotação do motor
        steps = input('Number of steps? (Can be negative)')
        state = rotate(state, steps)

try:
    main()
finally:
GPIO.cleanup()
    print("Fim de Programa!")
#END
