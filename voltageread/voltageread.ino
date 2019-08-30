void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  Serial.println("Voltage Reader");
}

void loop() {
  //top supply
  float voltage = 0;
  float current = 0;
  
  voltage = analogRead(A0);
  voltage *= (float)5/(0.27*1024);
  Serial.print("TV ");
  Serial.print(voltage);
  Serial.println(" V");

  current = analogRead(A1)*(float)5/(0.27*1000*1024);
  Serial.print("TA ");
  Serial.print(current);
  Serial.println(" A");
  
  //middle supply
  voltage = analogRead(A2)*(float)5/(0.27*1024);
  Serial.print("MV ");
  Serial.print(voltage);
  Serial.println(" V");
  
  current = analogRead(A3)*(float)5/(0.27*1000*1024);
  Serial.print("MA ");
  Serial.print(current);
  Serial.println(" A");
  
  //bottom supply
  
  voltage = analogRead(A4)*(float)5/(0.27*1024);
  Serial.print("BV ");
  Serial.print(voltage);
  Serial.println(" V");

  current = analogRead(A5)*(float)5/(0.27*1000*1024);
  Serial.print("BA ");
  Serial.print(current);
  Serial.println(" A");
  
  delay(1000);
}
