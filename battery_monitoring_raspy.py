"""
#!/usr/bin/env python
#title           :battery_monitoring_raspi.py
#description     :-
#author          :Fajar Muhammad Noor Rozaqi
#date            :2021/06/04
#version         :0.2
#usage           :BMS-python
#notes           :
#python_version  :3.9
#==============================================================================
"""

#library
import time
import datetime
import serial
import pymysql

#serial tx/rx pins on the GPIO header or USB
serial_port = '/dev/ttyUSB0'
#it must be same rate used on the Arduino
serial_rate = 9600

#function
def main():
    ser = serial.Serial(serial_port, serial_rate)
    ser.flushInput()
    while True:
        try:
            reading = ser.readline()
            reading = reading.decode("utf-8")
            reading = reading.rstrip()
            reading = reading.split(',')
            print(reading)

            #baterai 1
            timer = datetime.datetime.now()
            V_1 = str(reading[1])
            T_1 = str(reading[3])
            I_1 = str(reading[-1])
            print("Time            :",timer.strftime("%Y-%m-%d %H:%M:%S"))
            print("Voltage_1       :",V_1,"V")
            print("Temperature_1   :",T_1,"C")
            print("Current_1       :",I_1,"A")
            #Database Connection
            db = pymysql.connect(host='localhost',
                                 user='root',
                                 password='bmstest',
                                 db='monitoring')
            
            cur = db.cursor()
            
            try:
                add_c1 ="INSERT INTO `battery_monitoring`(time,voltage_1,temperature_1,current_1) VALUES(%s,%s,%s,%s)"
                cur.execute(add_c1,(timer.strftime("%Y-%m-%d %H:%M:%S"),
                                    V_1,
                                    T_1,
                                    I_1))
                db.commit()
                print("Data is sent")
                print("")
                
            except:
                db.rollback()
                print("Database is not connected")
                
            time.sleep(5)
            
        except:
            print("Raspberry Pi is NOT connected")
            break

if __name__ == "__main__":
    main() 