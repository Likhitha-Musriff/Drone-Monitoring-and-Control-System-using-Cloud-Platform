// Arduino code for reading GPS and camera data
#include <Wire.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_GPS.h>

Adafruit_GPS GPS(&Serial1);  // GPS sensor connection

void setup() {
  Serial.begin(9600);
  GPS.begin(9600);
}

void loop() {
  // Read GPS data
  while (GPS.available()) {
    char c = GPS.read();
    if (c == '$') {
      Serial.println("GPS Data: ");
      Serial.println(GPS.location.lat(), 6);
      Serial.println(GPS.location.lng(), 6);
    }
  }
}
