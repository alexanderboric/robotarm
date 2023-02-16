include <Stepper.h>;

String command;
const int stepsPerRevolution = 200;  // change this to fit the number of steps per revolution
// for your motor

// initialize the stepper library on pins 8 through 11:
Stepper myStepper(stepsPerRevolution, 8, 9, 10, 11);

void setup() {
  Serial.begin(9600);
  
  myStepper.setSpeed(60);


  Serial.println("Type Command ");
}

void loop() {
  if (Serial.available()) {
    command = Serial.readStringUntil('\n');
    command.trim();
    if (command.indexOf("move") > 0) {
      String myString= getValue(command,"move",1);
      String posX = getValue(myString, ',', 0);
      String posY = getValue(myString, ',', 1);
      String posZ = getValue(myString, ',', 2);

      String rotX = getValue(myString, ',', 3);
      String rotY = getValue(myString, ',', 4);
      String rotZ = getValue(myString, ',', 5);

    }
      Serial.print("du wolltest was bewegen");
    else {
      Serial.println("bad command");
    }
    Serial.print("Command: ");
    Serial.println(command);
  }

  // step one revolution in one direction:
  Serial.println("clockwise");
  myStepper.step(stepsPerRevolution);
  delay(500);

  // step one revolution in the other direction:
  Serial.println("counterclockwise");
  myStepper.step(-stepsPerRevolution);
  delay(500);
}
