#define  ADDO  7    //Data Out
#define  ADSK  6    //SCK

unsigned long ReadCount(); //conversão AD do HX711

unsigned long convert;

void setup(){
   pinMode(ADDO, INPUT_PULLUP);   //entrada paraatr receber os dados
   pinMode(ADSK, OUTPUT);         //saída para SCK
   
   Serial.begin(9600);
}

void loop(){
  	convert = ReadCount();
  
  	Serial.println(convert);
  
  	delay(2000);
}

unsigned long ReadCount(){
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

