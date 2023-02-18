#include <Stepper.h>;

String command;
const int stepsPerRevolution = 200;  // change this to fit the number of steps per revolution
// for your motor

// initialize the stepper library on pins 8 through 11:
Stepper myStepper(stepsPerRevolution, 8, 9, 10, 11);

void setup() {
  Serial.begin(9600);
  
  myStepper.setSpeed(10);
  Serial.println("Type Command ");
}

void loop() {
  if (Serial.available()) {
    command = Serial.readStringUntil('\n');
    command.trim();
    // Serial.println(command);
    Serial.println(command.indexOf("move"));
    if (command.indexOf("move") > 0) {
      Serial.print("du wolltest was bewegen");
      String myString = command.substring(command.indexOf(" "), command.length());//"move 1,2,3,4,5,6";
      Serial.println(myString);

    }  
    else {
      Serial.println("bad command");
    }
    Serial.print("Command: ");
    Serial.println(command);
  }

  // step one revolution in one direction:
  // Serial.println("clockwise");
  // myStepper.step(stepsPerRevolution);
  // delay(500);

  // // step one revolution in the other direction:
  // Serial.println("counterclockwise");
  // myStepper.step(-stepsPerRevolution);
  // delay(500);
}
