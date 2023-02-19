#include <AccelStepper.h>
const unsigned int NUM_STEPS = 4;

unsigned int xArray[NUM_STEPS] = {0, 50, 100, 150};
unsigned int xSpeeds[NUM_STEPS] = {200, 200, 200, 200};

const byte enablePin = 8;

AccelStepper x_stepper(AccelStepper::DRIVER, 2, 5);
static unsigned int index = 0;
void setup()
{
Serial.begin(115200);
pinMode(enablePin, OUTPUT);
digitalWrite(enablePin, LOW);
x_stepper.setAcceleration(2000);
x_stepper.setMaxSpeed(200);
x_stepper.setSpeed(200);
x_stepper.setCurrentPosition(0);
}

void loop()
{

if (x_stepper.run() == 0)
{
delay(250);
Serial.println(index);
x_stepper.moveTo(xArray[index]);
x_stepper.setMaxSpeed(xSpeeds[index]);
index++;
if (index >= NUM_STEPS)
{
index = 0;
x_stepper.setCurrentPosition(0);
delay(80);
}
}
}

