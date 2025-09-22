void setup() {
  Serial.begin(9600);
  randomSeed(analogRead(0));
}

void loop() {
  int vendorID = random(00, 30); // Simulated product IDs
  int rawMaterialID = random(00, 10); 
  double value = random(50, 10000);      // Quality percentage
  
  Serial.print(productID);
  Serial.print(",");
  Serial.println(quality);
  delay(1250);
}

