//Voltage-Temperature DS2438
//title           :ReadingVoltage-Temperatur.ino
//description     :SOC_OCV For Batteries.
//author          :Fajar Muhammad Noor Rozaqi
//date            :2021/04/28
//version         :0.3
//usage           :BMS
//notes           : testing single cell

//import library
#include <Arduino.h> 
#include <OneWire.h>  
#include <DS2438.h>  

//Variables  
char order;  

//float shuntvoltage_input = 0; //This variables only used if using IC MAX219 
//float busvoltage_input = 0;  
//float current_mA_input = 0;  
//float loadvoltage_input = 0;  
//float power_mW_input = 0;  
//float shuntvoltage_output = 0;  
//float busvoltage_output = 0;  
//float current_mA_output = 0;  
//float loadvoltage_output = 0;  
//float power_mW_output = 0;    

// Adressing Battery Sensor  
uint8_t bat1[8] = {0xA6, 0x27, 0x76, 0xFE, 0x0, 0x0, 0x50, 0x8B};  ////checking the addressing battery first

// Onewire-Pin
OneWire ow();  //checking the pin first

// DS2438 & addressing  
DS2438 sensor1(&ow, bat1);  

void setup() {  
    Serial.begin(9600);  
    sensor1.begin();  
    
    delay(100);  
    }  
    
void loop() {  
    if (Serial.available()>0){  
        order = Serial.read();  
        if (order == 'v'){  
            // Sensor Voltgae Baterai 1  
            sensor1.update();  
            if (sensor1.isError()) {  
                Serial.print("Error Reading");  
                Serial.print(" , ");  
            } else {
                    Serial.print("Sensor Volatage 1 = ");  
                    Serial.print(sensor1.getVoltage(DS2438_CHA)*1.347, 3);  
                    Serial.print(" , ");  
            }  
            
            // Sensor Temperature Baterai 1  
            sensor1.update();  
            if (sensor1.isError()) {  
                Serial.print("Error Reading");  
                Serial.print(" , ");  
            } else {
                    Serial.print("Sensor Temperature 1 = ");  
                    Serial.print(sensor1.getTemperature(DS2438_CHA), 3);  
                    Serial.print(" , ");  
            } 
	    }  
	    delay(1000);  

	    }  
	    else if (order == 'p'){  
	      Serial.print("Power Shield 1 is not installed")
          Serial.print(",")


          //This code below is only used if using IC MAX219
          // Sensor Input  
	      //shuntvoltage_input = sensorinput.getShuntVoltage_mV();  
	      //busvoltage_input = sensorinput.getBusVoltage_V();  
	      //current_mA_input = sensorinput.getCurrent_mA();  
	      //power_mW_input = sensorinput.getPower_mW();  
	      //loadvoltage_input = busvoltage_input + (shuntvoltage_input / 1000);  
	  
	      // Sensor output  
	      //shuntvoltage_output = sensoroutput.getShuntVoltage_mV();  
	      //busvoltage_output = sensoroutput.getBusVoltage_V();  
	      //current_mA_output = sensoroutput.getCurrent_mA();  
	      //power_mW_output = sensoroutput.getPower_mW();  
	      //loadvoltage_output = busvoltage_output + (shuntvoltage_output / 1000);  
	  
	      //Serial.print(power_mW_input,3);  
	      //Serial.print(" , ");  
	      //Serial.println(power_mW_output,3);  
	    }  
	  }  
	}
