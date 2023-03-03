//Register DS2438
//title           :ReadingDS2438.ino
//description     :DS2438 Register.
//author          :Fajar Muhammad Noor Rozaqi
//date            :2021/07/21
//version         :0.4
//usage           :BMS
//notes           :DS2438 Registers

//library
#include <OneWire.h>

//Variable
int V_AD = 0;
int I = 0;
int T = 0;
int ICA = 0;
int V_DD = 1;

//Voltage VAD
float VAD1,VAD2,VAD3,VAD4,VAD5,VAD6,VAD7,VAD8,VAD9,VAD10,VAD11,VAD12;
//Voltage VDD
float VDD1,VDD2,VDD3,VDD4,VDD5,VDD6,VDD7,VDD8,VDD9,VDD10,VDD11,VDD12;
//Current
float I1,I2,I3,I4,I5,I6,I7,I8,I9,I10,I11,I12;
//Temperature
float T1,T2,T3,T4,T5,T6,T7,T8,T9,T10,T11,T12;
//ICA (SoC ESTIMATION)
float ICA1,ICA2,ICA3,ICA4,ICA5,ICA6,ICA7,ICA8,ICA9,ICA10,ICA11,ICA12;

//pin connection ds2438
OneWire oneWire(4);

void setup() {
  Serial.begin(9600);
  delay(100);
}

void loop() {
  byte i;
  byte bat1[8] = {0x26, 0x84, 0x05, 0x1E, 0x02, 0x00, 0x00, 0xE7};
  byte bat2[8] = {0x26, 0xEE, 0x09, 0x1E, 0x02, 0x00, 0x00, 0xCA};
//  byte bat3[8] = {};
//  byte bat4[8] = {};
//  byte bat5[8] = {};
//  byte bat6[8] = {};
//  byte bat7[8] = {};
//  byte bat8[8] = {};
//  byte bat9[8] = {};
//  byte bat10[8] = {};
//  byte bat11[8] = {};
//  byte bat12[8] = {};

  //Voltage
  VAD1 = V_DS2438(bat1, V_AD);
  VAD2 = V_DS2438(bat2, V_AD);
//  VAD3 = V_DS2438(bat3, V_AD);
//  VAD4 = V_DS2438(bat4, V_AD);
//  VAD5 = V_DS2438(bat5, V_AD);
//  VAD6 = V_DS2438(bat6, V_AD);
//  VAD7 = V_DS2438(bat7, V_AD);
//  VAD8 = V_DS2438(bat8, V_AD);
//  VAD9 = V_DS2438(bat9, V_AD);
//  VAD10 = V_DS2438(bat10, V_AD);
//  VAD11 = V_DS2438(bat11, V_AD);
//  VAD12 = V_DS2438(bat12, V_AD);

  //Current
  I1 = I_DS2438(bat1, I);
  I2 = I_DS2438(bat2, I);
//  I3 = I_DS2438(bat3, I);
//  I4 = I_DS2438(bat4, I);
//  I5 = I_DS2438(bat5, I);
//  I6 = I_DS2438(bat6, I);
//  I7 = I_DS2438(bat7, I);
//  I8 = I_DS2438(bat8, I);
//  I9 = I_DS2438(bat9, I);
//  I10 = I_DS2438(bat10, I);
//  I11 = I_DS2438(bat11, I);
//  I12 = I_DS2438(bat12, I);
  
  //Temperature
  T1 = T_DS2438(bat1, T);
  T2 = T_DS2438(bat2, T);
//  T3 = T_DS2438(bat3, T);
//  T4 = T_DS2438(bat4, T);
//  T5 = T_DS2438(bat5, T);
//  T6 = T_DS2438(bat6, T);
//  T7 = T_DS2438(bat7, T);
//  T8 = T_DS2438(bat8, T);
//  T9 = T_DS2438(bat9, T);
//  T10 = T_DS2438(bat10, T);
//  T11 = T_DS2438(bat11, T);
//  T12 = T_DS2438(bat12, T);

  //ICA
  ICA1 = ICA_DS2438(bat1, ICA);
  ICA2 = ICA_DS2438(bat2, ICA);
//  ICA3 = ICA_DS2438(bat3, ICA);
//  ICA4 = ICA_DS2438(bat4, ICA);
//  ICA5 = ICA_DS2438(bat5, ICA);
//  ICA6 = ICA_DS2438(bat6, ICA);
//  ICA7 = ICA_DS2438(bat7, ICA);
//  ICA8 = ICA_DS2438(bat8, ICA);
//  ICA9 = ICA_DS2438(bat9, ICA);
//  ICA10 = ICA_DS2438(bat10, ICA);
//  ICA11 = ICA_DS2438(bat11, ICA);
//  ICA12 = ICA_DS2438(bat12, ICA);

  //Print Value
  //Baterai 1
  Serial.print(VAD1,2);
  Serial.print(" , ");
  Serial.print(I1,2);
  Serial.print(" , ");
  Serial.print(T1,2);
  Serial.print(" , ");
  Serial.print(ICA1,2);
  Serial.print(" , ");

  //Baterai 2
  Serial.print(VAD2,2);
  Serial.print(" , ");
  Serial.print(I2,2);
  Serial.print(" , ");
  Serial.print(T2,2);
  Serial.print(" , ");
  Serial.print(ICA2,2);
  Serial.print(" , ");

//  //Baterai 3
//  Serial.print(VAD3,2);
//  Serial.print(" , ");
//  Serial.print(I3,2);
//  Serial.print(" , ");
//  Serial.print(T3,2);
//  Serial.print(" , ");
//  Serial.print(ICA3,2);
//  Serial.print(" , ");
//
//  //Baterai 4
//  Serial.print(VAD4,2);
//  Serial.print(" , ");
//  Serial.print(I4,2);
//  Serial.print(" , ");
//  Serial.print(T4,2);
//  Serial.print(" , ");
//  Serial.print(ICA4,2);
//  Serial.print(" , ");
//
//  //Baterai 5
//  Serial.print(VAD5,2);
//  Serial.print(" , ");
//  Serial.print(I5,2);
//  Serial.print(" , ");
//  Serial.print(T5,2);
//  Serial.print(" , ");
//  Serial.print(ICA5,2);
//  Serial.print(" , ");
//
//  //Baterai 6
//  Serial.print(VAD6,2);
//  Serial.print(" , ");
//  Serial.print(I6,2);
//  Serial.print(" , ");
//  Serial.print(T6,2);
//  Serial.print(" , ");
//  Serial.print(ICA6,2);
//  Serial.print(" , ");
//
//  //Baterai 7
//  Serial.print(VAD7,2);
//  Serial.print(" , ");
//  Serial.print(I7,2);
//  Serial.print(" , ");
//  Serial.print(T7,2);
//  Serial.print(" , ");
//  Serial.print(ICA7,2);
//  Serial.print(" , ");
//
//  //Baterai 8
//  Serial.print(VAD8,2);
//  Serial.print(" , ");
//  Serial.print(I8,2);
//  Serial.print(" , ");
//  Serial.print(T8,2);
//  Serial.print(" , ");
//  Serial.print(ICA8,2);
//  Serial.print(" , ");
//
//  //Baterai 9
//  Serial.print(VAD9,2);
//  Serial.print(" , ");
//  Serial.print(I9,2);
//  Serial.print(" , ");
//  Serial.print(T9,2);
//  Serial.print(" , ");
//  Serial.print(ICA9,2);
//  Serial.print(" , ");
//
//  //Baterai 10
//  Serial.print(VAD10,2);
//  Serial.print(" , ");
//  Serial.print(I10,2);
//  Serial.print(" , ");
//  Serial.print(T10,2);
//  Serial.print(" , ");
//  Serial.print(ICA10,2);
//  Serial.print(" , ");
//
//  //Baterai 11
//  Serial.print(VAD11,2);
//  Serial.print(" , ");
//  Serial.print(I11,2);
//  Serial.print(" , ");
//  Serial.print(T11,2);
//  Serial.print(" , ");
//  Serial.print(ICA11,2);
//  Serial.print(" , ");
//
//  //Baterai 12
//  Serial.print(VAD12,2);
//  Serial.print(" , ");
//  Serial.print(I12,2);
//  Serial.print(" , ");
//  Serial.print(T12,2);
//  Serial.print(" , ");
//  Serial.println(ICA12,2);
  Serial.println("=============");
}

float V_DS2438(byte*addr, int source){
  int n;
  byte data[12];
  
  oneWire.reset();
  oneWire.select(addr);       //Match rom 0x55
  oneWire.write(0x4E);        //Write scratchpad
  oneWire.write(0x00);        //Page 0
  if (source == V_AD)         //Setup Vdd or Vad for A/D
    {
      oneWire.write(0x00);    //Input VAD //bit 5 Voltage A/D input select bit
    }
    else{
          oneWire.write(0x08);  //Input VDD // default 
        }
             
  oneWire.reset();
  oneWire.select(addr);
  oneWire.write(0xB4);  //Voltage Conversion
  delay(20);            //Wait for A/D to complete

  oneWire.reset();
  oneWire.select(addr);
  oneWire.write(0xB8);  //Recall memory to scratchpad
  oneWire.write(0x00);
  
  oneWire.reset();
  oneWire.select(addr);
  oneWire.write(0xBE);  //Read scratchpad
  oneWire.write(0x00);  
  
  for (n=0; n<9; n++)
    {
      data[n] = oneWire.read(); 
      //Serial.print(a[n]);
      //Serial.print("...?n");
      //delay(100);
    }  
  
  if ( OneWire::crc8(data, 8) != data[8]) {
    Serial.println("CRC is not valid!");
    return;
  }
  
  float Volt = ((((int16_t)data[4]) << 8) | data[3]) * 0.01;     // byte 3 Voltage LSB, byte 4 Voltage MSB
  
  return(Volt);
}

float I_DS2438(byte*addr, int source){
  int n;
  byte data[12];
  
  oneWire.reset();
  oneWire.select(addr);       //Match rom 0x55
  oneWire.write(0x4E);        //Write scratchpad
  oneWire.write(0x00);        //Page 0
  if (source == I)         //Setup Vdd or Vad for A/D
    {
      oneWire.write(0x00);    //Input VAD //bit 5 Voltage A/D input select bit
    }
    else{
          oneWire.write(0x08);  //Input VDD // default 
        }
             
  oneWire.reset();
  oneWire.select(addr);
  oneWire.write(0xB4);  //Voltage Conversion
  delay(20);            //Wait for A/D to complete

  oneWire.reset();
  oneWire.select(addr);
  oneWire.write(0x44); //Temperature Conversion
  delay(20);
  
  // Current readings are updated automatically
  
  oneWire.reset();
  oneWire.select(addr);
  oneWire.write(0xB8);  //Recall memory to scratchpad
  oneWire.write(0x00);
  
  oneWire.reset();
  oneWire.select(addr);
  oneWire.write(0xBE);  //Read scratchpad
  oneWire.write(0x00);  
  
  for (n=0; n<9; n++)
    {
      data[n] = oneWire.read(); 
      //Serial.print(a[n]);
      //Serial.print("...?n");
      //delay(100);
    }  
  
  if ( OneWire::crc8(data, 8) != data[8]) {
    Serial.println("CRC is not valid!");
    return;
  }
  
  float Iad = ((((int16_t)data[6]) << 8) | data[5] << 2) * 0.2441 / (4096 * 0.0005);
  
  return(Iad);
}

float T_DS2438(byte*addr, int source){
  int n;
  byte data[12];
  
  oneWire.reset();
  oneWire.select(addr);       //Match rom 0x55
  oneWire.write(0x4E);        //Write scratchpad
  oneWire.write(0x00);        //Page 0
  if (source == T)         //Setup Vdd or Vad for A/D
    {
      oneWire.write(0x00);    //Input VAD //bit 5 Voltage A/D input select bit
    }
    else{
          oneWire.write(0x08);  //Input VDD // default 
        }
             
  oneWire.reset();
  oneWire.select(addr);
  oneWire.write(0xB4);  //Voltage Conversion
  delay(20);            //Wait for A/D to complete

  oneWire.reset();
  oneWire.select(addr);
  oneWire.write(0x44); //Temperature Conversion
  delay(20);
  
  // Current readings are updated automatically
  
  oneWire.reset();
  oneWire.select(addr);
  oneWire.write(0xB8);  //Recall memory to scratchpad
  oneWire.write(0x00);
  
  oneWire.reset();
  oneWire.select(addr);
  oneWire.write(0xBE);  //Read scratchpad
  oneWire.write(0x00);  
  
  for (n=0; n<9; n++)
    {
      data[n] = oneWire.read(); 
      //Serial.print(a[n]);
      //Serial.print("...?n");
      //delay(100);
    }  
  
  if ( OneWire::crc8(data, 8) != data[8]) {
    Serial.println("CRC is not valid!");
    return;
  }
  
  float temp = (((((int16_t) data[2]) << 8) | data[1]) >> 3) * 0.03125;
  
  return(temp);
}

float ICA_DS2438(byte*addr, int source){
  int n;
  byte data[12];
  
  oneWire.reset();
  oneWire.select(addr);       //Match rom 0x55
  oneWire.write(0x4E);        //Write scratchpad
  oneWire.write(0x00);        //Page 0
  if (source == ICA)         //Setup Vdd or Vad for A/D
    {
      oneWire.write(0x00);    //Input VAD //bit 5 Voltage A/D input select bit
    }
    else{
          oneWire.write(0x08);  //Input VDD // default 
        }
             
  oneWire.reset();
  oneWire.select(addr);
  oneWire.write(0xB4);  //Voltage Conversion
  delay(20);            //Wait for A/D to complete

  oneWire.reset();
  oneWire.select(addr);
  oneWire.write(0x44); //Temperature Conversion
  delay(20);
  
  // Current readings are updated automatically
  
  oneWire.reset();
  oneWire.select(addr);
  oneWire.write(0xB8);  //Recall memory to scratchpad
  oneWire.write(0x00);
  
  oneWire.reset();
  oneWire.select(addr);
  oneWire.write(0xBE);  //Read scratchpad
  oneWire.write(0x00);  

  //ENABLING ICA, CCA, AND DCA ON SINGLE DS2438 (BUS MASTER COMMAND)  
  // Reading Page 1
  oneWire.reset();
  oneWire.select(addr);
  oneWire.write(0x4E); //write scratchpad
  oneWire.write(0x00); //page 0
  oneWire.write(0x0F); //Sets ICA, CA, EE, AD BITS ACTIVE

  // Read Scratchpad 0xBE
  oneWire.reset();
  oneWire.select(addr);
  oneWire.write(0xBE);
  oneWire.write(0x00); //Still not sure

  // Activate DS2438 BECOME 1
  oneWire.reset();
  oneWire.select(addr);
  oneWire.write(0x48);
  oneWire.write(0x00);
  oneWire.reset();
  
  //==================================================================================================== 
  // Reading Page 1
  oneWire.reset();
  oneWire.select(addr);
  oneWire.write(0x4E); //write scratchpad
  oneWire.write(0x01); //Page 1
  oneWire.write(0x01); //Page 1

  // Recall 0xB8
  oneWire.reset();
  oneWire.select(addr);
  oneWire.write(0xB8); // Recall 0xB8
  oneWire.write(0x01); // Page 1

  // Read Scratchpad 0xBE
  oneWire.reset();
  oneWire.select(addr);
  oneWire.write(0xBE);
  oneWire.write(0x01);
  
  for (n=0; n<9; n++)
    {
      data[n] = oneWire.read(); 
      //Serial.print(a[n]);
      //Serial.print("...?n");
      //delay(100);
    }  
  
  if ( OneWire::crc8(data, 8) != data[8]) {
    Serial.println("CRC is not valid!");
    return;
  }

  float ica = (data[4] * 0.4882 / (2048 * 0.0005));
  // if bat_nomical_capacity = 3.6 #Battery
  return(ica);
}
