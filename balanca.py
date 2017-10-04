import time
import os
import RPi.GPIO as GPIO

# Definir as portas
ADDO =     # Input Data
ADSK =     # Clock

unsigned long convert;

def gpio_setup(){

   GPIO.setmode(GPIO.BCM)
   
   GPIO.setup(ADDO, GPIO.IN, pull_up_down = GPIO.PUD_UP)    # Entrada para receber os dados
   GPIO.setup(ADSK, GPIO.OUT)   # Saída para o clock
}

def loop(){
  	convert = ReadCount();
  
  	Serial.println(convert);
  
  	delay(2000);
}

# Função para leitura efetiva do módulo ADC
def ReadCount(){
	unsigned long Count = 0;
	unsigned char i;
	  
	digitalWrite(ADSK, LOW);
	  
	while(digitalRead(ADDO));
	  
	for(i=0;i<24;i++){
		digitalWrite(ADSK, HIGH);
		Count = Count << 1;
		if(digitalRead(ADDO)) Count++;
                digitalWrite(ADSK, LOW);
	}
  
  	digitalWrite(ADSK, HIGH);
	Count = Count^0x800000;
	digitalWrite(ADSK, LOW);
  
	return(Count);
}
