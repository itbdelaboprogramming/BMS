//Finding One Wire address DS2438 battery
//title           :FindingBatteriesAddress.ino
//description     : For Battery Address
//author          :Fajar Muhammad Noor Rozaqi
//date            :2021/05/04
//version         :0.1
//usage           :BMS
//notes           : Use this script before fetching voltage and temperature of batteries

//import library
#include <Arduino.h> 
#include <OneWire.h>  
#include <DS2438.h>

//Script Finding Batteries address
if ( !oneWire.search(rom)) {
    //Serial.print("No more addresses.\n");
    Serial.println("==============================");
    oneWire.reset_search();
    delay(1000);
    x = 0;
    return;
}

//Testing if script finding addresses
//Voltage
Vad = MeasADC_2438(rom, V_AD);
Vdd = MeasADC_2438(rom, V_DD);
//Temperature
T = MeasTemperature_2438(rom);

//print value
Serial.print(T,3);
Serial.print(",");
Serial.print(Vad,2);
Serial.print(",");
Serial.print(Vdd,3);
Serial.print(",");
