//#define led_pin 13
#define sensor_pin A3
void setup() {
// put your setup code here, to run once:
//pinMode(sensor_pin, OUTPUT);
Serial.begin(9600);//скорость подключения
}

void loop() {
// put your main code here, to run repeatedly:
  int val = analogRead(sensor_pin);
  Serial.println(val);
  delay(20);
}