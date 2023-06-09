"""
#!/usr/bin/env python
#title           :Nepower_Kyuden_Battery_OCV_model.py
#description     :Polynomial Fitting For Kyuden Battery based on OCV method (offline).
#author          :Fajar Muhammad Noor Rozaqi
#date            :2023/06/05
#version         :0.1
#usage           :Battery Management System (BMS)
#notes           :Program is under review
#python_version  :3.8
#==============================================================================
"""

# Import library
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# import seaborn as sns
# sns.set(style="darkgrid")

# input: an nx2 .csv file of measurement number and Open Circuit Voltage (OCV)
# def csvToList(fileName):
#     dataFile = open(fileName, 'r')
#     unformattedData = dataFile.readlines()
#     formattedData = list()
#     # get rid of column titles
#     # del unformattedData[0]
#     # split the data by column, put in a formatted data list
#     for line in unformattedData:
#         currentLine = line.split(',')
#         measurementNumber = int(currentLine[0])
#         # print(measurementNumber)
#         voltage = float(currentLine[1])
#         # print(voltage)
#         formattedData.append([measurementNumber, voltage])
#         # print(formattedData)
#     dataFile.close()
#     return formattedData

# def excelTolList(fileName):
#     datafile = pd.read_excel(fileName)
#     measurementNumber = list(datafile[0])
#     voltage = list(datafile[1])

# Finds noisy data points in the experimental measurements of the cell's OCV
def findAnomalyIndex(dataList):
    anomalyIndexList = list()
    for i in range(len(dataList)):
        if i != 0:
            if dataList[i][1] - dataList[i-1][1] > .01:
                anomalyIndexList.append(i)
    return anomalyIndexList

# Corrects a noisy data point by taking the average of the 2 adjacent data points
def fixSingleAnomaly(anomalyIndex, dataSet):
    surroundingAverage = abs((dataSet[anomalyIndex + 1][1] + dataSet[anomalyIndex - 1][1])/2)
    # print(surroundingAverage)
    dataSet[anomalyIndex][1] = surroundingAverage
    # print(dataSet[anomalyIndex][0])

# Reverses the order of a list
def flipList(inputList):
    flippedList = list()
    for i in range(len(inputList)):
        flippedList.append(inputList[len(inputList) - i - 1])
    return flippedList

# Combines two lists to form a np.array
def createArray(listX, listY):
    newList = list()
    for i in range(len(listX)):
        newList.append([listX[i], listY[i]])
    return np.array(newList)

# Creates a list of values between min and max with defined spacing, similar to range but can do non-int spacing
def createSpacedList(min, max, spacing):
    currentVal = min
    spacedList = list()
    i = 0
    while currentVal < max:
        currentVal = min + (i * spacing)
        spacedList.append(currentVal)
        i += 1
    return spacedList

# Creates a list of the modeled nth order polynomial fit values
# input: order n of the polynomial fit, list of experimental x values, list of experimental y values
# returns: a list of the modeled y-values using the polynomial fit
def getPolyFitValues(order, xList, yList):
    coefficients = np.polyfit(xList, yList, order)
    modeledValues = list()
    for x in xList:
        yVal = 0
        i = 0
        while order - i >= 0:
            yVal += coefficients[i] * x ** (order - i)
            i += 1
        modeledValues.append(yVal)
    return modeledValues

# Finds the chi-square value for experimental and modeled values
def getChiSquaredValue(experimentalValues, modeledValues):
    # Calculate the chi-squared value
    totalChiSquared = 0
    for i in range(len(experimentalValues)):
        expectedValue = modeledValues[i]
        observedValue = experimentalValues[i]
        if expectedValue != 0:
            totalChiSquared += abs(((observedValue - expectedValue)**2) / expectedValue)
        elif abs(observedValue - expectedValue) <= 0.000001:
            totalChiSquared += 0
        else:
            totalChiSquared += (observedValue + expectedValue)**2
    return totalChiSquared

# Finds the optimal order n of a polynomial fit using minimum chi-square analysis
def findOptimalOrderFit(xValues, yValues):
    # Only checks order n=1:8 to minimize compute time
    n = 1
    chiSquaredResults = list()
    while n <=8:
        currentChiSquared = getChiSquaredValue(yValues, getPolyFitValues(n, xValues, yValues))
        chiSquaredResults.append([n, currentChiSquared])
        n += 1
    # find the minimum order n
    minIndex = 0
    minChiSquared = 1000000000000
    for i in range(len(chiSquaredResults)):
        if chiSquaredResults[i][1] < minChiSquared:
            minChiSquared = chiSquaredResults[i][1]
            minIndex = i
    # the returned object is of the form [order n, chi-squared value]
    return chiSquaredResults[minIndex]

# Prints the optimal order n, chi-squared value of the fit, and coefficients of the polynomial fit
def printFittingResults(chiSquaredResults, xValues, yValues):
    # prints the optimal order n
    print("Optimal Order Fit:", chiSquaredResults[0])
    # prints the chi-squared value of the fit
    print("Chi-Squared Value:", chiSquaredResults[1])
    # prints the coefficients of the optimal fit
    print("Coefficients:")
    coefficientList = np.polyfit(xValues, yValues, chiSquaredResults[0])
    order = chiSquaredResults[0]
    for i in range(len(coefficientList)):
        print("\tx" + str(order - i) +"\t=", coefficientList[i])

# Overview of Main
def main():

    # Get the data as a list from an nx2 .csv file
    
    # batteryData1 = csvToList('D:/BMS_OCV_Test.csv')
    # print(batteryData1)
    
    # batteryData1 = excelTolList("D:/BMS_OCV_Test_Lithium.xlsx")
    batteryData1 = csvToList('D:/BMS_OCV_TEST')

    # Separate measurement numbers and OCV readings into separate lists
    # measurementNumbers1 = list()
    # voltageReading1 = list()
    # for data in batteryData1:
    #     measurementNumbers1.append(data[0])
    #     voltageReading1.append(data[1])
    
    # for data in datafile:
    #     measurementNumbers1.append(data[0])
    #     voltageReading1.append(data[1])
    # print(measurementNumbers1)
    # print(voltageReading1)
    
    # Reading excel file
    datafile = pd.read_excel('D:/BMS_OCV_Test_Lithium.xlsx', header=None)
    measurementNumbers1 = list()
    voltageReading1 = list()
    measurementNumbers1 = list(datafile[0])
    voltageReading1 = list(datafile[1])
    # print(measurementNumbers1)
    # print(voltageReading1)
    # batteryData1 = list([measurementNumbers1,voltageReading1])
    def merge(measurementNumbers1, VoltageReading1):
        return [[a] + [b] for (a,b) in zip(measurementNumbers1,voltageReading1)]
    batteryData1 = (merge(measurementNumbers1,voltageReading1))

    # Find anomalies - used if discharge is interrupted or there are isolated noisy data points
    anomalies = findAnomalyIndex(batteryData1)

    # Fix any anomalies
    for anomaly in anomalies:
        fixSingleAnomaly(anomaly, batteryData1)

    # Refresh the lists with the corrected noisy data points
    measurementNumbers1 = list()
    voltageReading1 = list()
    for data in batteryData1:
        measurementNumbers1.append(data[0])
        voltageReading1.append(data[1])

    # Flip the order of the lists to allow for the SoC vs OCV plot
    measurementsAdjusted = flipList(measurementNumbers1)
    voltageReadingFinal = flipList(voltageReading1)

    # Normalize the data measurement numbers on a 0 to 100% scale
    numMeasurements = len(measurementsAdjusted)
    increment = 100.0/numMeasurements
    normalizedSoC = list()
    tempI = 0
    while tempI < numMeasurements:
        normalizedSoC.append(tempI*increment)
        tempI += 1

    # ----------------------------------------------------------------------------

    # Finds the optimal order n of a polynomial fit of the data using minimum chi-square analysis
    optimalFitValues = findOptimalOrderFit(voltageReadingFinal, normalizedSoC)
    optimalOrder = optimalFitValues[0]

    # Creates a list of modeled SoC values using the optimal polynomial fit, used for plotting
    modeledValues = getPolyFitValues(optimalOrder, voltageReadingFinal, normalizedSoC)

    # Prints the optimal order n, chi-squared value of the fit, and coefficients of the polynomial fit
    print("\nFITTING RESULTS")
    print("---------------")
    printFittingResults(optimalFitValues, voltageReadingFinal, normalizedSoC)

    # PLOTTING
    showRawData = True

    if showRawData:
        # Plots the raw OCV vs measurement number data
        plt.subplot(1, 2, 1)
        plt.plot(measurementNumbers1, voltageReading1, label='Raw Data')
        plt.legend(loc='best')
        plt.xlabel('Measurement Number')
        plt.ylabel('Cell Voltage (V)')
        plt.title("Raw Data - Open Circuit Voltage (OCV)\nvs Measurement Number", fontweight='bold')
        plt.grid(True)
        # Plots the experimental SoC vs OCV
        plt.subplot(1, 2, 2)
        plt.plot(normalizedSoC, voltageReadingFinal, label='Experimental Data Lithium 2021/06/17 ')
        # Plots the modeled values using the polynomial fit for SoC vs OCV
        plt.plot(modeledValues,voltageReadingFinal, label='Polynomial Fit')
        plt.legend(loc='best')
        plt.xlabel('State of Charge (%)')
        plt.ylabel('Cell Voltage (V)')
        plt.title("Battery State of Charge (SoC) vs\nOpen Circuit Voltage (OCV)", fontweight='bold')
        plt.grid(True)
        # Adjust spacing of subplots
        plt.subplots_adjust(wspace=0.35)
    else:
        # Plots the experimental SoC vs OCV
        plt.plot(normalizedSoC, voltageReadingFinal, label='Experimental Data Lithium 2021/06/17')
        # Plots the modeled values using the polynomial fit for SoC vs OCV
        plt.plot(modeledValues, voltageReadingFinal, label='Polynomial Fit')
        plt.legend(loc='best')
        plt.xlabel('State of Charge (%)')
        plt.ylabel('Cell Voltage (V)')
        plt.title("Battery State of Charge (SoC) vs\nOpen Circuit Voltage (OCV)", fontweight='bold')
        plt.grid(True)
        # Adjust spacing of subplots
        plt.subplots_adjust(wspace=0.35)

    plt.show()

main()
