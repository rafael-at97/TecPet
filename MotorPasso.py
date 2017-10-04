// Conexões do "primeiro" motor
int IN1 = 8;
int IN2 = 9;
// Conexões do "segundo" motor
int IN3 = 10;
int IN4 = 11;

/*Tabela de sequência para os passos*/
bool sequence[4][4] = {   {1, 0, 0, 1},
                          {0, 1, 0, 1},
                          {0, 1, 1, 0},
                          {1, 0, 1, 0}
 };

void setup(){
  // Define os pinos como saida
  pinMode(IN1,OUTPUT);
  pinMode(IN2,OUTPUT);
  pinMode(IN3,OUTPUT);
  pinMode(IN4,OUTPUT);
}

int tempo = 10;

void rotate(int &state, int steps){
    for(int i = 0; i < abs(steps); i++){
        state = (state + steps/abs(steps) + 4)%4;
        digitalWrite(IN1, sequence[state][0]);
        digitalWrite(IN2, sequence[state][1]);
        digitalWrite(IN3, sequence[state][2]);
        digitalWrite(IN4, sequence[state][3]);
    };
    delay(tempo);
}

void loop(){
  int state = 0;
  
  rotate(state, 5);
}
