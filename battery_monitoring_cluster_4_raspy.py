"""
#!/usr/bin/env python
#title           :battery_monitoring_raspi.py
#description     :-
#author          :Fajar Muhammad Noor Rozaqi
#date            :2021/08/04
#version         :0.3
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
serial_port = '/dev/ttyUSB4'
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
            timer1 = datetime.datetime.now()
            V_1 = str(reading[1])
            I_1 = str(reading[3])
            T_1 = str(reading[5])
            ICA_1 = str(reading[7])

            #baterai 2
            timer2 = timer1
            V_2 = str(reading[9])
            I_2 = str(reading[11])
            T_2 = str(reading[13])
            ICA_2 = str(reading[15])

            #baterai 3
            timer3 = timer2
            V_3 = str(reading[17])
            I_3 = str(reading[19])
            T_3 = str(reading[21])
            ICA_3 = str(reading[23])

            #baterai 4
            timer4 = timer3
            V_4 = str(reading[25])
            I_4 = str(reading[27])
            T_4 = str(reading[29])
            ICA_4 = str(reading[31])

            #baterai 5
            timer5 = timer4
            V_5 = str(reading[33])
            I_5 = str(reading[35])
            T_5 = str(reading[37])
            ICA_5 = str(reading[39])

            #baterai 6
            timer6 = timer5
            V_6 = str(reading[41])
            I_6 = str(reading[43])
            T_6 = str(reading[45])
            ICA_6 = str(reading[47])

            #baterai 7
            timer7 = timer6
            V_7 = str(reading[49])
            I_7 = str(reading[51])
            T_7 = str(reading[53])
            ICA_7 = str(reading[55])

            #baterai 8
            timer8 = timer7
            V_8 = str(reading[57])
            I_8 = str(reading[59])
            T_8 = str(reading[61])
            ICA_8 = str(reading[63])

            #baterai 9
            timer9 = timer8
            V_9 = str(reading[65])
            I_9 = str(reading[67])
            T_9 = str(reading[69])
            ICA_9 = str(reading[71])

            #baterai 10
            timer10 = timer9
            V_10 = str(reading[73])
            I_10 = str(reading[75])
            T_10 = str(reading[77])
            ICA_10 = str(reading[79])

            #baterai 11
            timer11 = timer10
            V_11 = str(reading[81])
            I_11 = str(reading[83])
            T_11 = str(reading[85])
            ICA_11 = str(reading[87])

            #baterai 12
            timer12 = timer11
            V_12 = str(reading[89])
            I_12 = str(reading[91])
            T_12 = str(reading[93])
            ICA_12 = str(reading[95])

            print("Time            :",timer1.strftime("%Y-%m-%d %H:%M:%S"))
            print("Voltage_1       :",V_1,"V")
            print("Current_1       :",I_1,"A")
            print("Temperature_1   :",T_1,"C")
            print("ICA_1           :",ICA_1,"Ah")
            print("")
            
            print("Time            :",timer2.strftime("%Y-%m-%d %H:%M:%S"))
            print("Voltage_2       :",V_2,"V")
            print("Current_2       :",I_2,"A")
            print("Temperature_2   :",T_2,"C")
            print("ICA_2           :",ICA_2,"Ah")
            print("")

            print("Time            :",timer3.strftime("%Y-%m-%d %H:%M:%S"))
            print("Voltage_3       :",V_3,"V")
            print("Current_3       :",I_3,"A")
            print("Temperature_3   :",T_3,"C")
            print("ICA_3           :",ICA_3,"Ah")
            print("")

            print("Time            :",timer4.strftime("%Y-%m-%d %H:%M:%S"))
            print("Voltage_4       :",V_4,"V")
            print("Current_4       :",I_4,"A")
            print("Temperature_4   :",T_4,"C")
            print("ICA_4           :",ICA_4,"Ah")
            print("")

            print("Time            :",timer5.strftime("%Y-%m-%d %H:%M:%S"))
            print("Voltage_5       :",V_5,"V")
            print("Current_5       :",I_5,"A")
            print("Temperature_5   :",T_5,"C")
            print("ICA_5           :",ICA_5,"Ah")
            print("")
            
            print("Time            :",timer6.strftime("%Y-%m-%d %H:%M:%S"))
            print("Voltage_6       :",V_6,"V")
            print("Current_6       :",I_6,"A")
            print("Temperature_6   :",T_6,"C")
            print("ICA_6           :",ICA_6,"Ah")
            print("")

            print("Time            :",timer7.strftime("%Y-%m-%d %H:%M:%S"))
            print("Voltage_7       :",V_7,"V")
            print("Current_7       :",I_7,"A")
            print("Temperature_7   :",T_7,"C")
            print("ICA_7           :",ICA_7,"Ah")
            print("")

            print("Time            :",timer8.strftime("%Y-%m-%d %H:%M:%S"))
            print("Voltage_8       :",V_8,"V")
            print("Current_8       :",I_8,"A")
            print("Temperature_8   :",T_8,"C")
            print("ICA_8           :",ICA_8,"Ah")
            print("")

            print("Time            :",timer9.strftime("%Y-%m-%d %H:%M:%S"))
            print("Voltage_9       :",V_9,"V")
            print("Current_9       :",I_9,"A")
            print("Temperature_9   :",T_9,"C")
            print("ICA_9           :",ICA_9,"Ah")
            print("")

            print("Time            :",timer10.strftime("%Y-%m-%d %H:%M:%S"))
            print("Voltage_10       :",V_10,"V")
            print("Current_10       :",I_10,"A")
            print("Temperature_10   :",T_10,"C")
            print("ICA_10           :",ICA_10,"Ah")
            print("")

            print("Time            :",timer11.strftime("%Y-%m-%d %H:%M:%S"))
            print("Voltage_11       :",V_11,"V")
            print("Current_11       :",I_11,"A")
            print("Temperature_11   :",T_11,"C")
            print("ICA_11           :",ICA_11,"Ah")
            print("")

            print("Time            :",timer12.strftime("%Y-%m-%d %H:%M:%S"))
            print("Voltage_12       :",V_12,"V")
            print("Current_12       :",I_12,"A")
            print("Temperature_12   :",T_12,"C")
            print("ICA_12           :",ICA_12,"Ah")
            print("")

            #Database Connection
            db = pymysql.connect(host='localhost',
                                 user='root',
                                 password='bmstest',
                                 db='monitoring')
            
            cur = db.cursor()
            
            try:
                add_c1 ="INSERT INTO `battery_monitoring_cluster_4`(time,voltage_1,current_1,temperature_1,capacity_1,voltage_2,current_2,temperature_2,capacity_2,voltage_3,current_3,temperature_3,capacity_3,voltage_4,current_4,temperature_4,capacity_4,voltage_5,current_5,temperature_5,capacity_5,voltage_6,current_6,temperature_6,capacity_6,voltage_7,current_7,temperature_7,capacity_7,voltage_8,current_8,temperature_8,capacity_8,voltage_9,current_9,temperature_9,capacity_9,voltage_10,current_10,temperature_10,capacity_10,voltage_11,current_11,temperature_11,capacity_11,voltage_12,current_12,temperature_12,capacity_12) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                cur.execute(add_c1,(timer.strftime("%Y-%m-%d %H:%M:%S"),
                                    V_1,
                                    I_1,
                                    T_1,
                                    ICA_1,
                                    V_2,
                                    I_2,
                                    T_2,
                                    ICA_2,
                                    V_3,
                                    I_3,
                                    T_3,
                                    ICA_3,
                                    V_4,
                                    I_4,
                                    T_4,
                                    ICA_4,
                                    V_5,
                                    I_5,
                                    T_5,
                                    ICA_5,
                                    V_6,
                                    I_6,
                                    T_6,
                                    ICA_6,
                                    V_7,
                                    I_7,
                                    T_7,
                                    ICA_7,
                                    V_8,
                                    I_8,
                                    T_8,
                                    ICA_8,
                                    V_9,
                                    I_9,
                                    T_9,
                                    ICA_9,
                                    V_10,
                                    I_10,
                                    T_10,
                                    ICA_10,
                                    V_11,
                                    I_11,
                                    T_11,
                                    ICA_11,
                                    V_12,
                                    I_12,
                                    T_12,
                                    ICA_12))
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