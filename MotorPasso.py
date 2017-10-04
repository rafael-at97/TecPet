import time
import os
import RPi.GPIO as GPIO
import numpy as np

# Conexões do "primeiro" motor
IN1 = 
IN2 = 
# Conexões do "segundo" motor
IN3 = 
IN4 = 

# Tabela de sequência para os passos
sequence = np.array([[1,0,0,1], [0,1,0,1], [0,1,1,0], [1,0,1,0]])

tempo = 10

def gpio_setup():
  # Define os pinos como saida
  GPIO.setmode(GPIO.BCM)
  
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

def main():
  gpio_setup()
  state = 0
  
  while True:
      steps = input('Number of steps? (Can be negative)')
      state = rotate(state, steps)

try:
    main()
finally:
    GPIO.cleanup()
    print("Fim de Programa!")
#END  
