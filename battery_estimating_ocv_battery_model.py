"""
#!/usr/bin/env python
#title           :=.py
#description     :OCV Battery Model For Batteries.
#author          :Fajar Muhammad Noor Rozaqi
#date            :2021/11/01
#version         :0.1
#usage           :BMS-python
#notes           :
#python_version  :3.8
#==============================================================================
"""
# Description

# Import Library
import numpy as np # library numpy is used for Python programming languange as operation array.
import matplotlib.pyplot as plt # library matplotlib is used for plotting the graph

def ConvertingCSVToListData (fileNameCsv):
    filecsv = open(fileNameCsv, 'r')
    filecsvUnformattedData = filecsv.readlines() # readlines() method returns a list containing each line in the file as a list item
    filecsvFormattedData = list() # list() function is used for creating a list object on a python language
    # del filecsvUnformattedData[0] # Deleting  the column titles
    # Spliting the data by column, and converting into a formatted data list
    for line in filecsvUnformattedData:
        initialLine = line.split(',')
        data = int(initialLine[0])
        voltage =  float(initialLine[1])
        filecsvFormattedData.append([data, voltage])
    filecsv.close()
    return filecsvFormattedData

def NoisyDataList(fileNameList):
    NoisyData = list()
    for i in range(len(fileNameList)) # len() function stands for returning the number of items in a a list
                                      # range(len(()) is used for together when iterating over a mutable sequemce

def main():

    # Step 1 : Reading the data  from csv, and converting into list
    batteryData = ConvertingCSVToListData('D:/BMS_OCV_Test.csv')
    # print(batteryData)

    dataMeasurement = list()
    voltage = list()
    for data in batteryData:
        dataMeasurement.append(data[0])
        voltage.append(data[1])
    
    # print(dataMeasurement)
    # print(voltage)

    # Step 2 : Checking the battery data list, if there is an empty data
main()
