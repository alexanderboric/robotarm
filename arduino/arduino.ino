#include <Stepper.h>;
#include <AccelStepper.h>;

//max speed 345 bei 960 steps per revolution 

String command;
int stepsPerRevolution = 800;  // change this to fit the number of steps per revolution
// for your motor

// initialize the stepper library on pins 8 through 11:
Stepper stepperX(stepsPerRevolution, 2,5);
//AccelStepper xStepper(8,2,3,4,5,true);
Stepper stepperY(stepsPerRevolution, 3,6);
Stepper stepperZ(stepsPerRevolution, 4,7);
Stepper stepperA(stepsPerRevolution, 12,13);

//AccelStepper myAccStepper(1, 2, 3, 4, 5);

void setup() {
  // xStepper.setMaxSpeed(300);
  // xStepper.setSpeed(100);
  // xStepper.setAcceleration(100);
  Serial.begin(9600);
  stepperX.setSpeed(100);
  stepperY.setSpeed(100);
  stepperZ.setSpeed(100);
  stepperA.setSpeed(100);
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
      Serial.print("starting test");
      String myString = command.substring(command.indexOf(" "), command.length());//"move 1,2,3,4,5,6";
      Serial.println(myString);

    }
    else if (command.indexOf("stop") >= 0) {
      is_testing=false;
      //xStepper.stop();
      Serial.println("test stoped");
      String myString = command.substring(command.indexOf(" "), command.length());//"move 1,2,3,4,5,6";
      Serial.println(myString);

    }
    else if (command.indexOf("set speed") >= 0) {
      String myString = command.substring(command.lastIndexOf(" "), command.length());//"move 1,2,3,4,5,6";
      myStepper.setSpeed(myString.toInt());
      //xStepper.setSpeed(myString.toInt());
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
    //move_angle(stepperX, 360);
    move_all_angle(360);
    //xStepper.move(stepsPerRevolution);
    delay(500);

    // step one revolution in the other direction:
    //Serial.println("counterclockwise");
    //move_angle(stepperX, -360);
    move_all_angle(-360);
    //xStepper.move(-stepsPerRevolution);
    delay(500);
  }
  


}

  
void move_angle(Stepper s, int angle){
  s.step(int(float(float(stepsPerRevolution)/float(360))*float(angle)));
  //Serial.print("moved ");
  //Serial.println(int(float(float(stepsPerRevolution)/float(360))*float(angle)));
}

void move_all_angle(int angle){
  move_angle(stepperX, angle);
  move_angle(stepperY, angle);
  move_angle(stepperZ, angle);
  move_angle(stepperA, angle);
}

// Ramp for interpolation