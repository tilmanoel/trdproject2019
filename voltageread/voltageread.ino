void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
//  Serial.println("Voltage Reader");
}

void loop() {
  //top supply
  float voltage = 0;
  float current = 0;
  
  voltage = (float)analogRead(A0)/1024;
  Serial.print("TV ");
  Serial.print(voltage);
  Serial.println(" V");

  current = (float)analogRead(A1)/1024;
  Serial.print("TA ");
  Serial.print(current);
  Serial.println(" A");
  
  //middle supply
  voltage = (float)analogRead(A2)/1024;
  Serial.print("MV ");
  Serial.print(voltage);
  Serial.println(" V");
  
  current = (float)analogRead(A3)/1024;
  Serial.print("MA ");
  Serial.print(current);
  Serial.println(" A");
  
  //bottom supply
  
  voltage = (float)analogRead(A4)/1024;
  Serial.print("BV ");
  Serial.print(voltage);
  Serial.println(" V");

  current = (float)analogRead(A5)/1024;
  Serial.print("BA ");
  Serial.print(current);
  Serial.println(" A");
  
  delay(1000);
}
