"""
#!/usr/bin/env python
#title           :battery_monitoring_raspy_with_csv.py
#description     :-
#author          :Fajar Muhammad Noor Rozaqi
#date            :2021/04/15
#version         :0.2
#usage           :BMS-python
#notes           :
#python_version  :3.9
#==============================================================================
"""

#library
from os import write
import time
import datetime
from typing import ValuesView
import serial
import pymysql

#serial tx/rx pins on the GPIO header or USB
serial_port = '/dev/ttyUSB0'
#it must be same rate used on the Arduino
serial_rate = 9600

#test
print("test")
print("")

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
            I_1 = str(reading[3])
            T_1 = str(reading[-1])
            
            print("Time            :",timer.strftime("%Y-%m-%d %H:%M:%S"))
            print("Voltage_1       :",V_1,"V")
            print("Current_1       :",I_1,"A")
            print("Temperature_1   :",T_1,"C")
            
            #Database Connection
            db = pymysql.connect(host='localhost',
                                 user='root',
                                 password='bmstest',
                                 db='monitoring')
            
            cur = db.cursor()
            
            try:
                add_c1 ="INSERT INTO `battery_monitoring`(time,voltage_1,current_1,temperature_1) VALUES(%s,%s,%s,%s)"
                cur.execute(add_c1,(timer.strftime("%Y-%m-%d %H:%M:%S"),
                                    V_1,
                                    I_1,
                                    T_1))
                db.commit()
                print("Data is sent")
                print("")

                #Reading Record Database 
                try:
                    with db.cursor() as cursor:
                        sql = "SELECT date(time),(voltage_1),(current_1),(temperature_1) FROM `battery_monitoring`"
                        cursor.execute(sql)
                        result = cursor.fetchall()
                        print(result)
                    
                    #Converting into CSV File
                    with open("/home/pi/batterylog.csv", mode='w', newline='') as csvfile:

                        file = csv.writer(csvfile, delimeter =',')
                        file.writerow(['time','voltage_1','current_1','temperature_1'])
                        for i in range(0, len(result)):
                            file.writerow(result[i].values())
                            time.append(result[i]['time'])
                            voltage1.append(result[i]['voltage_1'])
                            current1.append(result[i]['current_1'])
                            temperature1.append(result[i]['temperature_1'])
                except:
                    print("CSV is not converted")
                
            except:
                db.rollback()
                print("Database is not connected")
                
            time.sleep(5)
            
        except:
            print("Raspberry Pi is NOT connected")
            break

if __name__ == "__main__":
    main()
