#include <OneWire.h>

int V_AD = 0;
int V_Bat = 0;
int V_DD = 1;
int bus = 3;
float Vad1,Vad2,Vad3,Vad4,Vad5,Vad6,Vad7,Vad8,Vad9,Vad10;
float Vad11,Vad12,Vad13,Vad14,Vad15,Vad16,Vad17,Vad18,Vad19,Vad20;
char order;

int x;

OneWire oneWire(bus);

void setup(){
  Serial.begin(9600);
  delay(100);
}

void loop(){
    byte i;
    byte bat1[8] = {0xA6, 0x27, 0x76, 0xFE, 0x0, 0x0, 0x50, 0x8B};
    byte bat2[8] = {0xA6, 0x9D, 0xE0, 0x93, 0x0, 0x0, 0x50, 0x65};
    byte bat3[8] = {0xA6, 0x33, 0xF9, 0xD3, 0x0, 0x0, 0x50, 0x45};
    byte bat4[8] = {0xA6, 0x23, 0xD6, 0x12, 0x1, 0x0, 0x50, 0x94};
    byte bat5[8] = {0xA6, 0xD8, 0x15, 0xD7, 0x0, 0x0, 0x50, 0x61};
    byte bat6[8] = {0xA6, 0x44, 0xCB, 0x12, 0x1, 0x0, 0x50, 0x42};
    byte bat7[8] = {0xA6, 0x71, 0xFC, 0x84, 0x0, 0x0, 0x50, 0xD2};
    byte bat8[8] = {0xA6, 0xEB, 0xAA, 0x1E, 0x1, 0x0, 0x50, 0xF4};
    byte bat9[8] = {0xA6, 0x29, 0xA, 0xD7, 0x0, 0x0, 0x50, 0x37};
    byte bat10[8] = {0xA6, 0xB3, 0x80, 0xFE, 0x0, 0x0, 0x50, 0xDC};
    byte bat11[8] = {0xA6, 0x51, 0x63, 0x2E, 0x1, 0x0, 0x50, 0xA5};
    byte bat12[8] = {0xA6, 0xF4, 0x19, 0xA7, 0x0, 0x0, 0x50, 0x23};
    byte bat13[8] = {0xA6, 0x23, 0xF0, 0xFA, 0x0, 0x0, 0x50, 0xE};
    byte bat14[8] = {0xA6, 0xF0, 0x11, 0x2D, 0x1, 0x0, 0x50, 0xA8};
    byte bat15[8] = {0xA6, 0xA, 0x11, 0xD4, 0x0, 0x0, 0x50, 0x5C};
    byte bat16[8] = {0xA6, 0x8, 0xFE, 0xD4, 0x0, 0x0, 0x50, 0x87};
    byte bat17[8] = {0xA6, 0x7E, 0xBD, 0xD9, 0x0, 0x0, 0x50, 0x97};
    byte bat18[8] = {0xA6, 0x3E, 0x15, 0xD7, 0x0, 0x0, 0x50, 0xFA};
    byte bat19[8] = {0xA6, 0x8C, 0xCF, 0xD9, 0x0, 0x0, 0x50, 0x65};
    byte bat20[8] = {0xA6, 0xAC, 0x7F, 0xFE, 0x0, 0x0, 0x50, 0x6A};
    
    float Vad, Vdd;
    
    Vad1 = MeasADC_2438(bat1, V_AD);
    Vad2 = MeasADC_2438(bat2, V_AD);
    Vad3 = MeasADC_2438(bat3, V_AD);
    Vad4 = MeasADC_2438(bat4, V_AD);
    Vad5 = MeasADC_2438(bat5, V_AD);
    Vad6 = MeasADC_2438(bat6, V_AD);
    Vad7 = MeasADC_2438(bat7, V_AD);
    Vad8 = MeasADC_2438(bat8, V_AD);
    Vad9 = MeasADC_2438(bat9, V_AD);
    Vad10 = MeasADC_2438(bat10, V_AD);
    Vad11 = MeasADC_2438(bat11, V_AD);
    Vad12 = MeasADC_2438(bat12, V_AD);
    Vad13 = MeasADC_2438(bat13, V_AD);
    Vad14 = MeasADC_2438(bat14, V_AD);
    Vad15 = MeasADC_2438(bat15, V_AD);
    Vad16 = MeasADC_2438(bat16, V_AD);
    Vad17 = MeasADC_2438(bat17, V_AD);
    Vad18 = MeasADC_2438(bat18, V_AD);
    Vad19 = MeasADC_2438(bat19, V_AD);
    Vad20 = MeasADC_2438(bat20, V_AD);
     
    Serial.print(Vad1,2);
    Serial.print(" , ");
    Serial.print(Vad2,2);
    Serial.print(" , ");
    Serial.print(Vad3,2);
    Serial.print(" , ");
    Serial.print(Vad4,2);
    Serial.print(" , ");
    Serial.print(Vad5,2);
    Serial.print(" , ");
    Serial.print(Vad6,2);
    Serial.print(" , ");
    Serial.print(Vad7,2);
    Serial.print(" , ");
    Serial.print(Vad8,2);
    Serial.print(" , ");
    Serial.print(Vad9,2);
    Serial.print(" , ");
    Serial.print(Vad10,2);
    Serial.print(" , ");
    Serial.print(Vad11,2);
    Serial.print(" , ");
    Serial.print(Vad12,2);
    Serial.print(" , ");
    Serial.print(Vad13,2);
    Serial.print(" , ");
    Serial.print(Vad14,2);
    Serial.print(" , ");
    Serial.print(Vad15,2);
    Serial.print(" , ");
    Serial.print(Vad16,2);
    Serial.print(" , ");
    Serial.print(Vad17,2);
    Serial.print(" , ");
    Serial.print(Vad18,2);
    Serial.print(" , ");
    Serial.print(Vad19,2);
    Serial.print(" , ");
    Serial.println(Vad20,2);
}

float MeasADC_2438(byte*rom, int source){
    int n;
    byte a[9];
            
    oneWire.reset();
    oneWire.select(rom);       // match rom 0x55
    oneWire.write(0x4e);       // write scratchpad
    oneWire.write(0x00);       // page 0
    if (source == V_AD)        // setup Vdd or Vad for A/D
    {
        oneWire.write(0x00);  // input Vad // bit 5 Voltage A/D input select bit
    }
    else
    {
        oneWire.write(0x08);  // input Vdd // default 
    }     

    oneWire.reset();
    oneWire.select(rom);
    oneWire.write(0xb4);  // perform A/D
//    delay(100);          // wait for A/D to complete

    oneWire.reset();
    oneWire.select(rom);
    oneWire.write(0xb8);  // recall memory to scratchpad
    oneWire.write(0x00);

    oneWire.reset();
    oneWire.select(rom);
    oneWire.write(0xbe);  // read scratchpad
    oneWire.write(0x00);  
 
    for (n=0; n<9; n++)
    {
        a[n] = oneWire.read(); 
        //Serial.print(a[n]);
        //Serial.print("...?n");
        //delay(100);
    }  
    
    float Volt;
    
    Volt = (float)(a[4] * 256 + a[3]) * 0.01;      // byte 3 Voltage LSB, byte 4 Voltage MSB
    
    
    return(Volt);    
}
