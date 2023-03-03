#include "DHT.h"
#define DHTPIN 2
#define DHTTYPE DHT11   // DHT 11
#include <Servo.h>

DHT dht(DHTPIN, DHTTYPE);
Servo myDoor;

String myCmd;
int red = 3;
int yellow = 4;
int motor = 6;

//int trigPin = 12;
//int echoPin = 11;
//int pingTravelTime;
//float pingTravelDistance;
//float distanceToTarget;

int door = 9;

void turnMotorON();
void turnMotorOFF();
void tempHumid();
//void distanceMeasure();

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(red, OUTPUT);
  pinMode(yellow, OUTPUT);

  pinMode(motor, OUTPUT);

//  pinMode(trigPin, OUTPUT);
//  pinMode(echoPin, INPUT);

  dht.begin();

  myDoor.attach(door);

  digitalWrite(red, LOW);
  digitalWrite(yellow, LOW);
}

void loop() {
  // put your main code here, to run repeatedly:
//  distanceMeasure();

  while (Serial.available() == 0) {}
  myCmd = Serial.readStringUntil('\r');
  myCmd.toLowerCase();

  if (myCmd == "11") {
    digitalWrite(red, HIGH);
  }
  if (myCmd == "10") {
    digitalWrite(red, LOW);
  }
  if (myCmd == "21") {
    digitalWrite(yellow, HIGH);
  }
  if (myCmd == "20") {
    digitalWrite(yellow, LOW);
  }
  if (myCmd == "all1") {
    digitalWrite(red, HIGH);
    digitalWrite(yellow, HIGH);
  }
  if (myCmd == "all0") {
    digitalWrite(red, LOW);
    digitalWrite(yellow, LOW);
  }
  if (myCmd == "31") {
    turnMotorON();
  }
  if (myCmd == "30") {
    turnMotorOFF();
  }

  if (myCmd == "4") {
    tempHumid();
  }

  if (myCmd == "51" || myCmd == "511") {
    myDoor.write(180);
  }

  if (myCmd == "50" || myCmd == "500") {
    myDoor.write(90);
  }

  //  delay(100);
}

void turnMotorON() {
  digitalWrite(motor, HIGH);
}

void turnMotorOFF() {
  digitalWrite(motor, LOW);
}

void tempHumid() {
  float h = dht.readHumidity();
  // Read temperature as Celsius (the default)
  float t = dht.readTemperature();
  // Read temperature as Fahrenheit (isFahrenheit = true)
  float f = dht.readTemperature(true);

  Serial.print(t);
  Serial.print(",");
  Serial.println(h);
}

//void distanceMeasure() {
//  digitalWrite(trigPin, LOW);
//  delayMicroseconds(10);
//  digitalWrite(trigPin, HIGH);
//  delayMicroseconds(10);
//  digitalWrite(trigPin, LOW);
//
//  pingTravelTime = pulseIn(echoPin, HIGH);
//  delay(25);
//  pingTravelDistance = (pingTravelTime * 765.*5280.*12) / (3600.*1000000);
//  distanceToTarget = pingTravelDistance / 2;
//
//  Serial.println(distanceToTarget);
//}
