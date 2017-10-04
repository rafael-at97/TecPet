import time
import os
import RPi.GPIO as GPIO

# Definição dos pinos das boias (Boia_1 superior e Boia_2 inferior)
Boia_1 = 
Boia_2 = 

def gpio_setup():
    # Definição de modo da biblioteca RPi.GPIO:
    # GPIO.BOARD = Número dos pinos no esquemático da placa
    # GPIO.BCM   = Número de "Broadcom SOC Channel", escritos depois de "GPIO" no esquemático da placa
    GPIO.setmode(GPIO.BCM)
    # Definição das boias como normalmente abertas
    GPIO.setup(Boia_1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(Boia_2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def main ():
    gpio_setup()
    while True:
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

try:
    main()
finally:
    GPIO.cleanup()
    print("Fim de Programa!")
    #END
