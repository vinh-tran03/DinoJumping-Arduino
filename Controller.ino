const int jumpButton = 2;
const int crouchButton = 3;

void setup() {
  pinMode(jumpButton, INPUT_PULLUP);
  pinMode(crouchButton, INPUT_PULLUP);
  Serial.begin(9600);
}

void loop() {
  if (digitalRead(jumpButton) == LOW) {
    Serial.println("J");
    delay(200); // debounce
  }

  if (digitalRead(crouchButton) == LOW) {
    Serial.println("C");
    delay(200); // debounce
  }
}
