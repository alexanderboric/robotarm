#include <Stepper.h>;
#include <AccelStepper.h>;

String command;
int stepsPerRevolution = 800;  // change this to fit the number of steps per revolution
// for your motor

// initialize the stepper library on pins 8 through 11:
Stepper myStepper(stepsPerRevolution, 2,3,4,5);

//AccelStepper myAccStepper(1, 2, 3, 4, 5);

void setup() {
  Serial.begin(9600);
  myStepper.setSpeed(100);
  Serial.println("Type Command ");
}


bool is_testing=false;
void loop() {

  if (Serial.available() > 0) {
    delay(1000);
    //Serial.println("Serial connected at : " + String(millis()) + "ms");
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
      //myAccStepper.run();
      Serial.print("starting test");
      String myString = command.substring(command.indexOf(" "), command.length());//"move 1,2,3,4,5,6";
      Serial.println(myString);

    }
    else if (command.indexOf("stop") >= 0) {
      is_testing=false;
      //myAccStepper.stop();
      Serial.println("test stoped");
      String myString = command.substring(command.indexOf(" "), command.length());//"move 1,2,3,4,5,6";
      Serial.println(myString);

    }
    else if (command.indexOf("set speed") >= 0) {
      String myString = command.substring(command.lastIndexOf(" "), command.length());//"move 1,2,3,4,5,6";
      myStepper.setSpeed(myString.toInt());
      //myAccStepper.setSpeed(myString.toInt());
      Serial.println("speed set to "+ myString);

    }
    else if (command.indexOf("set stepsPerRevelution") >= 0) {
      String myString = command.substring(command.lastIndexOf(" "), command.length());//"move 1,2,3,4,5,6";
      stepsPerRevolution=myString.toInt(); 
      Serial.println("Steps per revolution set to "+myString);

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
    //Serial.println("testing");
    //step one revolution in one direction:
    //Serial.println("clockwise");
    move_angle(myStepper, 90);
    //myAccStepper.move(stepsPerRevolution);
    delay(500);

    // step one revolution in the other direction:
    //Serial.println("counterclockwise");
    move_angle(myStepper, -90);
    //myAccStepper.move(-stepsPerRevolution);
    delay(500);
  }
  


}

  
void move_angle(Stepper s, int angle){
  s.step(800/360*angle);
}

