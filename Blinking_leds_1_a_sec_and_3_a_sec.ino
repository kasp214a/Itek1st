
int tick = 0; // 

void setup() {

  pinMode(7,OUTPUT);
  pinMode(8,OUTPUT);
 
}


// turns on LED after every 3 ticks and off after 6 ticks 
void blinklong() {
  if (tick == 3){
    digitalWrite(7,HIGH); 
    }
  if (tick == 6){
    digitalWrite(7,LOW);
    tick = 0; 
    }
}
// checks if LED is on if so turns if off and other wise turns it off 
void blinkfast() {
  if (digitalRead(8) == HIGH){
    digitalWrite(8,LOW); 
}
  else
    digitalWrite(8,HIGH);

}

void loop(){
  blinklong();
  blinkfast();
  delay(167);
  tick += 1; // tick up every 0.167 seconds
}
