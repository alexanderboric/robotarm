#include <Stepper.h>;

class Segment{
    public:
        Segment(int length, int [3] rotation ,int [3] bottomPositon, int [3] topPosition, rMin,rMax, stepsPerRevolution=200, maxSpeed, int [4] pins){
            Stepper myStepper(stepsPerRevolution, pins[0], pins[1], pins[2], pins[3]);
            this->length = length;
            this->rotation = rotation; // rotation axis (defines which axis is able to rotate but only relative to the previeous segment)
            this->bottomPositon = bottomPositon;
            this->topPosition = topPosition;
            this->rMin = rMin;
            this->rMax = rMax;
            this->stepsPerRevolution = stepsPerRevolution;
            this->maxSpeed = maxSpeed;
        }
        void setLength(int length){
            this->length = length;
        }
        void setRotation(int [3] rotation){
            this->rotation = rotation;
        }
        void setBottomPosition(int [3] bottomPosition){
            this->bottomPosition = bottomPosition;
        }
        void setTopPosition(int [3] topPosition){
            this->topPosition = topPosition;
        }
        void setRMin(int rMin){
            this->rMin = rMin;
        }
        void setRMax(int rMax){
            this->rMax = rMax;
        }
        void setStepsPerRevolution(int stepsPerRevolution){
            this->stepsPerRevolution = stepsPerRevolution;
        }
        void setMaxSpeed(int maxSpeed){
            this->maxSpeed = maxSpeed;
        }
        int getLength(){
            return this->length;
        }
        int [3] getRotation(){
            return this->rotation;
        }
        int [3] getBottomPosition(){
            return this->bottomPosition;
        }
        int [3] getTopPosition(){
            return this->topPosition;
        }
        int getRMin(){
            return this->rMin;
        }
        int getRMax(){
            return this->rMax;
        }
        int getStepsPerRevolution(){
            return this->stepsPerRevolution;
        }
        int getMaxSpeed(){
            return this->maxSpeed;
        }

        void calculatePosition(int [3] bottomPosition,int [3] topPosition, int [3] rotation){
            //calculating the true rotation axis based on the rotation of the previous segment
            this->bottomPosition = bottomPosition;

            int [3] absRotation = rotation[0],;
            
        }

        }

        
};