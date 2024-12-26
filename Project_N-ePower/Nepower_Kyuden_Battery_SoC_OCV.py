#!/usr/bin/env python
#title           :Nepower_Kyuden_Battery_SoC_OCV.py
#description     :SOC OCV (Open Circuit Voltage) method For Kyuden Battery.
#author          :Fajar Muhammad Noor Rozaqi
#date            :2024/11/01
#version         :0.3
#usage           :BMS-Python
#notes           :
#python_version  :3.9.7
#==============================================================================

# Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Define coefficients for the polynomial
POLYNOMIAL_COEFFICIENTS = {
    'x11': 1.7738173870072556e-18,
    'x10': -4.801327471977691e-15,
    'x9': 5.560620735462417e-12,
    'x8': -3.482397700973714e-09,
    'x7': 1.1567625787124435e-06,
    'x6': -8.933932249320343e-05,
    'x5': -0.09253353703659696,
    'x4': 45.253376176605954,
    'x3': -10545.003853169965,
    'x2': 1421098.0573940529,
    'x1': -106515278.96156228,
    'x0': 3458910194.4554205
}

def evaluate_polynomial(v):
    """
    Evaluate the polynomial for SOC estimation given a voltage value.
    Args:
        v (float): Voltage value.
    Returns:
        float: Estimated SOC value.
    """
    coeffs = POLYNOMIAL_COEFFICIENTS
    return (coeffs['x11'] * v**11 + coeffs['x10'] * v**10 + coeffs['x9'] * v**9 + 
            coeffs['x8'] * v**8 + coeffs['x7'] * v**7 + coeffs['x6'] * v**6 + 
            coeffs['x5'] * v**5 + coeffs['x4'] * v**4 + coeffs['x3'] * v**3 + 
            coeffs['x2'] * v**2 + coeffs['x1'] * v + coeffs['x0'])

def read_data(file_path):
    """
    Read and preprocess data from an Excel file.
    Args:
        file_path (str): Path to the Excel file.
    Returns:
        tuple: Tuple containing time and voltage series.
    """
    data = pd.read_excel(file_path)
    time = pd.Series(np.ravel(data.iloc[:, 0])).dropna()  # Column A for time
    voltage = pd.Series(np.ravel(data.iloc[:, 2])).dropna()  # Column C for voltage
    min_length = min(len(time), len(voltage))
    return time[:min_length], voltage[:min_length]

def estimate_soc(voltage_series):
    """
    Estimate SOC for each voltage value in the series.
    Args:
        voltage_series (pd.Series): Series of voltage values.
    Returns:
        pd.Series: Estimated SOC values.
    """
    return pd.Series([evaluate_polynomial(v) for v in voltage_series]).dropna()

def plot_soc_estimation(time_series, soc_series):
    """
    Plot the SOC estimation over time.
    Args:
        time_series (pd.Series): Series of time values.
        soc_series (pd.Series): Series of estimated SOC values.
    """
    plt.figure(figsize=(10, 5))
    plt.plot(time_series, soc_series, label='SOC Estimate (OCV Method)', color='blue', lw=0.75)
    plt.xlabel('Time')
    plt.ylabel('SOC (%)')
    plt.title('SOC Estimation Over Time')
    plt.legend()
    plt.grid(True)
    plt.show()

def main():
    """
    Main function to execute the SOC estimation process.
    """
    print("==== Estimation of SOC Battery ====")
    file_path = 'D:/discharging2_filtered.xlsx'
    time_series, voltage_series = read_data(file_path)
    soc_series = estimate_soc(voltage_series)
    print("Estimated SOC values:")
    print(soc_series)
    plot_soc_estimation(time_series, soc_series)

if __name__ == '__main__':
    main()