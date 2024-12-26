import pandas as pd
import numpy as np
import os
import time
from INA219 import INA219
from ECC import estimate_initial_soc_from_ocv, DCRfromSoC

# Battery and sampling configuration
max_capacity_ah = 5
time_intervals = 0.5

def calculate_soc(max_capacity_ah, current_values, time_intervals, current_charge):
    charge_added_ah = current_values * time_intervals/3600
    current_charge += charge_added_ah
    return current_charge / max_capacity_ah*100, current_charge

ina219 = INA219(i2c_bus=1,addr=0x43)
low = 0
intialVoltage = ina219.getBusVoltage_V()
initialSoC = estimate_initial_soc_from_ocv(intialVoltage)
initalDCR = DCRfromSoC(initialSoC)
initialCurrent = ina219.getCurrent_mA()/1000
initialSoC = estimate_initial_soc_from_ocv(intialVoltage+initialCurrent*initalDCR)
currentCapacity = 0 # in Ah
while True:
    bus_voltage = ina219.getBusVoltage_V()             # voltage on V- (load side)
    shunt_voltage = ina219.getShuntVoltage_mV() / 1000 # voltage between V+ and V- across the shunt
    current = -ina219.getCurrent_mA()                   # current in mA
    power = ina219.getPower_W()                        # power in W
    p,currentCapacity = calculate_soc(max_capacity_ah,current,time_intervals,currentCapacity)
    if(p > 100):p = 100
    if(p < 0):p = 0

    # INA219 measure bus voltage on the load side. So PSU voltage = bus_voltage + shunt_voltage
    #print("PSU Voltage:   {:6.3f} V".format(bus_voltage + shunt_voltage))
    #print("Shunt Voltage: {:9.6f} V".format(shunt_voltage))
    print("""
          Load Voltage:  {:6.3f} V
          Current:       {:6.3f} A
          Power:         {:6.3f} W
          Percent:       {:3.1f}%""" %(bus_voltage,current/1000,power,p))
    
    if(bus_voltage < 3.15) and (current < 50):
        low += 1
        if(low >= 30):
            print("System shutdown now")
            address = os.popen("i2cdetect -y -r 1 0x2d 0x2d | egrep '2d' | awk '{print $2}'").read()
            if(address!='2d\n'):
                print("0x2d i2c address not detected, something wrong.")
            else:
                print("If charged, the system can be powered on again")
                #write 0x55 to 0x01 register of 0x2d Address device
                os.popen("i2cset -y 1 0x2d 0x01 0x55")
            os.system("sudo poweroff")
        else:
            print("Voltage Low,please charge in time,otherwise it will shut down in {:2d} s".format(60-2*low))
    else:
        low = 0

    time.sleep(time_intervals)

