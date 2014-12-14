#include <Stepper.h>

const int stepsPerRevolution = 4;  // change this to fit the number of steps per revolution
                                     // for your motor

// initialize the stepper library on pins 8 through 11:
Stepper myStepper(stepsPerRevolution, 8,9);

void setup() {
  // set the speed at 60 rpm:
  myStepper.setSpeed(60);
  // initialize serial communication:
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
      case 'b':    
        myStepper.step(-stepsPerRevolution);
        Serial.print(0);
        delay(100);
        break;
      }
    }
  }
}
