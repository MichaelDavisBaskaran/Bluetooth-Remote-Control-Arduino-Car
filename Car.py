#include <AFMotor.h>



void setup() {
  Serial.begin(9600);
}

void loop() {
    if (Serial.avaliable() > 0){
      command = Serial.read();
      Stop();
   
      switch(command){
        case 'F':
          forward();
          break;
        case 'B'
        |
          backward();
          break;
        /*case 'L':
          left();
          break;
        case 'R':
          right();
          break;*/
       
      }
    }
}

void forward(){
motor1.setSpeed(200);
motor1.run(FORWARD);
motor2.setSpeed(200);
motor2.run(FORWARD);
motor3.setSpeed(200);
motor3.run(FORWARD);
motor4.setSpeed(200);
motor4.run(FORWARD);
}

void Stop(){
  motor1.setSpeed(0);
  motor1.run(RELEASE);
  motor2.setSpeed(0);
  motor2.run(RELEASE);
  motor3.setSpeed(0);
  motor3.run(RELEASE);
  motor4.setSpeed(0);
  motor4.run(RELEASE);
 
}

void back(){
  motor1.setSpeed(200);
  motor1.run(BACKWARD);
  motor2.setSpeed(200);
  motor2.run(BACKWARD);
  motor3.setSpeed(200);
  motor3.run(BACKWARD);
  motor4.setSpeed(200);
  motor4.run(BACKWARD);
}