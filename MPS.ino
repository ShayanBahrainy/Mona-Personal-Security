#include <Stepper.h>
#include <Servo.h>



#define STEP 300

Stepper stepper(STEP,11,10);  
Servo servo_1; // create servo object to control a servo
Servo servo_2;


void move_arm(int position) {
  servo_1.write(position);
  servo_2.write(-position);
}

const int MAX_ROTATION = 600;
int rotation = 0;
int dir = 1;
int increment = 10;

void setup() {
  pinMode(6, OUTPUT);
  servo_1.attach(3);
  servo_2.attach(4);
  delay(1000);
  stepper.setSpeed(30);
  move_arm(120);
}


void loop() {
 if (!Serial.available()) {
    if (abs(rotation) > MAX_ROTATION) {
      dir *= -1;
    }
    rotation += increment * dir;
    stepper.step(increment * dir);
    return;
 }
 String x_ratio_string = Serial.readStringUntil('\n');
 String y_ratio_string = Serial.readStringUntil('\n');
 bool shoot = Serial.readStringUntil('\n') == "True";
 float x_ratio = std::atof(x_ratio_string.c_str());
 float y_ratio = std::atof(y_ratio_string.c_str());
 rotation += increment * x_ratio;
 stepper.step(increment * x_ratio);
 move_arm(120);
 if (shoot) {
  digitalWrite(6, HIGH);
  delay(1000);
  digitalWrite(6, LOW);
 }
 
}
