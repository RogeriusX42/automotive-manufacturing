void setup() {
  Serial.begin(9600);
  randomSeed(analogRead(0));
}

void loop() {
  int productID = random(00, 50); // Simulated product IDs
  int quality = random(40, 100);      // Quality percentage
  Serial.print(productID);
  Serial.print(",");
  Serial.println(quality);
  delay(1000);
}