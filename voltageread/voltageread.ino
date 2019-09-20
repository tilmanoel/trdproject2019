void setup() {

  Serial.begin(9600);
}

void loop() {

  Serial.print("TV ");
  Serial.print(analogRead(A0));
  Serial.println(" V");
  Serial.print("TA ");
  Serial.print(analogRead(A1));
  Serial.println(" A");
  Serial.print("MV ");
  Serial.print(analogRead(A2));
  Serial.println(" V");
  Serial.print("MA ");
  Serial.print(analogRead(A3));
  Serial.println(" A");
  Serial.print("BV ");
  Serial.print(analogRead(A4));
  Serial.println(" V");
  Serial.print("BA ");
  Serial.print(analogRead(A5));
  Serial.println(" A");
  delay(1000);
}
