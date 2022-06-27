"""
#!/usr/bin/env python
#title           :canbusMSD700.py
#description     :CAN-BUS Communication between SCiB Battery and Raspberry Pi
#author          :Fajar Muhammad Noor Rozaqi
#date            :2021/12/02
#version         :0.1
#usage           :BMS-python
#notes           :
#python_version  :3.8
#==============================================================================
"""

# Import library
import can # code packet for canbus communication
import time # RTC Real Time Clock

# Specifications of Socket CAN (Check first the type)
bustype = 'socketcan_cytapes' # Types of socket
channel = 'can0' # location of channel used for CAN BUS Communication

# Checking the connection "CAN-BUS"
try:
    # Default speed of CANBUS = 500000
    canbus0 = can.interface.Bus(bustype=bustype, channel=channel, bitrate= 500000)
    canbus0.connect()
    print("Conected to CANBUS Communication")
except:
    print("Cannot find CANBUS Communication")
    canbus0.close()

# Reading a CANBUS Message
while True:
    try:
        # recv() method for reading from the bus (in here we are using a SCiB Battery)
        canbus_message = canbus0.recv()
        scib_battery_data = canbus_message.arbitration_id
        # time counter
        timer = datetime.datetime.now()

        # Converting HEX Data from CAN BUS into demical, first it need manual book communication SCiB Battery
        # Not yet

        # Print the data
        print("Time         :", timer.strftime("%Y-%m-%d %H:%M")) # Time
        print("Battery data :", scib_battery_data)

        # Delay
        time.sleep(5)

        # Database Connection
        db = pymysql.connect(host='localhost',
                            user='root',
                            password='scibbattery',
                            db='scib')
            
        cur = db.cursor()

        add_c0 = "INSERT INTO `monitoring_scib`(battery_data, date_entered) VALUES (%s,%s)"
        cur.execute(add_c0,((scib_battery_data,
                            timer.strftime("%Y-%m-%d %H:%M"))))
        db.commit()
    
    except:
        # print("============")
        # print("Disconnected")
        # print("============")
        # time.sleep(0)
        pass
