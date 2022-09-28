    #define sensor_pin A2
    void setup() {
    Serial.begin(9600);
    pinMode(LED_BUILTIN, OUTPUT);
    }

    void loop() {
    int val = analogRead(sensor_pin);
    Serial.println(val);
    delay(10);
    if (val < 850){
      digitalWrite(LED_BUILTIN, HIGH);   // turn the LED on (HIGH is the voltage level)
      delay(100);
    }
    else{
      digitalWrite(LED_BUILTIN, LOW);    // turn the LED off by making the voltage LOW
      delay(100); 
    }
                           // wait for a second
    
    }

