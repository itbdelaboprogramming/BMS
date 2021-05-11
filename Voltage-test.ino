//Voltage-Temperature DS2438
//title           :ReadingVoltage-Temperatur.ino
//description     :SOC_OCV For Batteries.
//author          :Fajar Muhammad Noor Rozaqi
//date            :2021/04/28
//version         :0.3
//usage           :BMS
//notes           : testing single cell and sending to raspberry pi

//library
#include <OneWire.h>
#include <DS2348.h>

// define the Arduino digital I/O pin to be used for the 1-Wire network here
// define the 1-Wire address of the DS2438 battery monitor here (lsb first)
uint8_t bat1[8] = {0x26, 0xCE, 0xDD, 0x1D, 0x02, 0x00, 0x00, 0xB5};
uint8_t bat2[8] = {0x26, 0x0B, 0x15, 0x1E, 0x02, 0x00, 0x00, 0x55};

//Define OneWire Pin
OneWire ow(3);

//DS2438 & ADDRESSING
DS2438 sensor1(&ow, bat1);
DS2438 sensor2(&ow, bat2);

void setup() {
    Serial.begin(9600);
    sensor1.begin();
    sensor2.begin();
    delay(100);
}

void loop() {
  // 1st Battery Sensor 
    sensor1.update();
    if (sensor1.isError()) {
        Serial.print("Error Reading 1st Battery");
        Serial.print(" , ");
    } else {
        Serial.print("Voltage 1 = ");
        Serial.print(sensor1.getVoltage(DS2438_CHA)*1.347, 3);
        Serial.print(" , ");
    }

    // 2nd Battery Sensor
    sensor2.update();
    if (sensor2.isError()) {
        Serial.print("Error Reading 2nd Battery");
        Serial.print(" , ");
    } else {
        Serial.print("Voltage 2 = ");
        Serial.print(sensor2.getVoltage(DS2438_CHA)*1.367, 3);
        Serial.print(" , ");
    }

    Serial.println("-----");
    delay(1000);
}