String data;
int relay_mic = 13;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(relay_mic, OUTPUT);
  // Serial1.begin(11)
}

void loop() {
  // put your main code here, to run repeatedly:
  // Serial.println(Serial.read());
  if(Serial.available() > 0)
    {
      data = Serial.readString();
      if(data == "1"){
        digitalWrite(relay_mic, 1);
        Serial.print("on");
      }
      if(data == "0"){
        digitalWrite(relay_mic, 0);
        Serial.print("off");
      }
    }
}
