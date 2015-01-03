#include <Stepper.h>

const int stepsPerRevolution = 4;
Stepper myStepper(stepsPerRevolution, 8,9);

void setup() {
  myStepper.setSpeed(60);
  Serial.begin(9600);
}

void loop() {
  while (Serial.available()) {
    delay(30);
    if (Serial.available() > 0) {
      int inByte = Serial.read();
      switch (inByte) {
        case 'a':    
          myStepper.step(stepsPerRevolution);
          Serial.flush();
          Serial.print(1);
          delay(100);
          break;
        }
    }
  }
}
