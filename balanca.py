import time
import os
import RPi.GPIO as GPIO

# Definir as portas
ADDO =     # Input Data
ADSK =     # Clock

def gpio_setup():

   GPIO.setmode(GPIO.BCM)
   
   GPIO.setup(ADDO, GPIO.IN, pull_up_down = GPIO.PUD_UP)    # Entrada para receber os dados
   GPIO.setup(ADSK, GPIO.OUT)   # Saída para o clock

# Função para leitura efetiva do módulo ADC
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

def main():
	gpio_setup()
	
	while True :
  		convert = ReadCount()
  
  		print(convert)
  
  		time.sleep(2000)
	
try:
    main()
finally:
    GPIO.cleanup()
    print("Fim de Programa!")
#END
