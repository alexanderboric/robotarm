#include <Stepper.h>;

String command;
const int stepsPerRevolution = 200;  // change this to fit the number of steps per revolution
// for your motor

// initialize the stepper library on pins 8 through 11:
Stepper myStepper(stepsPerRevolution, 2,5);

void setup() {
  Serial.begin(9600);
  
  myStepper.setSpeed(10);
  Serial.println("Type Command ");
}


bool is_testing=false;
void loop() {

  if (Serial.available() > 0) {
    delay(1000);
    Serial.println("Serial connected at : " + String(millis()) + "ms");

    command = Serial.readStringUntil('\n');
    
    command.trim();
    // Serial.println(command);
    Serial.println(command.indexOf("move"));
    if (command.indexOf("move") >= 0) {
      Serial.print("du wolltest was bewegen");
      String myString = command.substring(command.indexOf(" "), command.length());//"move 1,2,3,4,5,6";
      Serial.println(myString);

    }
    else if (command.indexOf("test") >= 0) {
      is_testing=true;
      Serial.print("starting test");
      String myString = command.substring(command.indexOf(" "), command.length());//"move 1,2,3,4,5,6";
      Serial.println(myString);

    }
    else if (command.indexOf("stop") >= 0) {
      is_testing=false;
      Serial.print("test stoped");
      String myString = command.substring(command.indexOf(" "), command.length());//"move 1,2,3,4,5,6";
      Serial.println(myString);

    }
    else {
      Serial.println("bad command");
    }
    Serial.print("Command: ");
    Serial.println(command);
    Serial.flush();
    
  }
  delay(500);

  if(is_testing){
    Serial.println("testing");
    //step one revolution in one direction:
    Serial.println("clockwise");
    myStepper.step(stepsPerRevolution);
    delay(500);

    // step one revolution in the other direction:
    Serial.println("counterclockwise");
    myStepper.step(-stepsPerRevolution);
    delay(500);
  }
  


}

  


