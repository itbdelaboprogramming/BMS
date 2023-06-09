"""
#!/usr/bin/env python
#title           :Nepower_Kyuden_Battery_SoC_OCV.py
#description     :SOC OCV (Open Circuit Voltage) method For Kyuden Battery.
#author          :Fajar Muhammad Noor Rozaqi
#date            :2023/06/05
#version         :0.1
#usage           :BMS-python
#notes           :Program/Algorithm is under review
#python_version  :3.8
#==============================================================================
"""

#import library
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import time
from datetime import datetime
import csv
# import seaborn as sns
# sns.set(style="darkgrid")

#start of program
start = time.time()

#Algorithm of SOC Estimation Battery
print("====+++++++++++++++++++++++++====")
print("====+++++++++++++++++++++++++====")
print("====+++++++++++++++++++++++++====")
print("====Estimation of SOC Battery====")
print("====+++++++++++++++++++++++++====")
print("====+++++++++++++++++++++++++====")
print("====+++++++++++++++++++++++++====")

#first array
#sub of battery
v_soc = []
i_soc = []
soc = []

#sub of time
time_soc = []

#Reading of Battery
# with open('D:/mppt_4f_six.csv', newline='') as f:
#     reader = csv.reader(f)
#     for row in reader:
#         print(row)
data_soc = pd.read_csv('D:/BMS_test1.csv')

#initiation of data reading
v_soc = data_soc['BatVolt']
v_soc = pd.Series(np.ravel(v_soc)).dropna()
i_soc = data_soc['BatCur']
i_soc = pd.Series(np.ravel(i_soc)).dropna()
time_soc = data_soc['time']
time_soc = pd.to_datetime(np.ravel(time_soc)).dropna()
# time_soc = pd.Series(np.ravel(time_soc)).dropna()

##plotting V,I,T based on reading
# plt.style.use('dark_background')
# figure, ax1 = plt.subplots(figsize=(9.7,4.5))
# color = 'orange'
# ax1.set_xlabel('time (yyyy-mm-ddThh:mm:ssZ)', fontsize=12)
# ax1.set_ylabel('Battery Voltage (V)',fontsize=12)
# ax1.plot(time_0, v_0,label='Battery Voltage (V)', color=color, lw=0.5)
# ax1.tick_params(axis='y')
# # axes = plt.gca()
# # axes.set_ylim([25,34])
# ax1.legend(loc='lower left')
# ax1.grid()

# ax2 = ax1.twinx()
# color = 'blue'
# ax2.set_ylabel('Battery Current (A)',fontsize=12)
# ax2.plot(time_0, i_0,label='Battery Current (A)', color=color, lw=0.5)
# ax2.tick_params(axis='y')
# # axes = plt.gca()
# # axes.set_ylim([-15,15])
# figure.tight_layout()
# ax2.legend(loc='lower right')
# plt.figure(1).savefig('Test 1', quality=100)
# # plt.style.use('dark_background')

#Estimation of SOC Battery
def SOC_estimation():

	# #Initial value
	# capacity = 116*2
	# SOC = 50 #initial soc had to be tuned first
	# dt = 1/60

	# #Estimation SOC with CC Method
	# SOC_cc = []
	# for i, data in enumerate(i_0):
	# 	# I = i_0[i]
	# 	SOC = SOC + ((i_0[i]*dt)/capacity)
	# 	SOC_cc.append(SOC)
	# SOC_cc = pd.Series(np.ravel(SOC_cc)).dropna()
	# print(SOC_cc)

	#Estimation Soc with OCV 7th order
	SOC_ocv = []
	soc = []

	for i, data in enumerate(v_soc):
		x8  	= 0
		x7	= 0
		x6	= 2.237762467861503
		x5	= 0.03418556060441675
		x4	= -4.243089817994437
		x3	= 209.72587338311544
		x2	= -5160.391592686133
		x1	= 63224.4109174412
		x0	= -308656.73942473787
		
		v = v_soc[i]
		soc = (((v**8)*0)+((v**7)*0)+((v**6)*0)+((v**5)*x5)+((v**4)*x4)+((v**3)*x3)+((v**2)*x2)+((v**1)*x1)+((v**0)*x0))
		SOC_ocv.append(soc)
	SOC_ocv = pd.Series(np.ravel(SOC_ocv)).dropna()
	print(SOC_ocv)
	
	# # Plotting
	# cm = plt.cm.get_cmap('jet_r')

	# plt.figure(figsize=(11,5))
	# graph = plt.scatter(time_soc, SOC_ocv,
	# 				 lw=0.1, c=SOC_ocv,
	# 				 alpha=0.5, label="SOC_ocv",
	# 				 cmap=cm,vmin=0, vmax=100, s=10)
	# plt.plot(time_soc, SOC_ocv,lw=0.5, c='black',alpha=0.25)
	# plt.colorbar(graph)
	# # plt.avxspan(pd.to_datetime())
	# plt.xlabel("time (yyyy-mm-ddThh:mm:ssZ)", fontsize=12)
	# plt.ylabel("SOC Battery(%)", fontsize=12)
	# plt.legend(loc="lower right")
	# # plt.xlim(42,50)
	# # plt.ylim(0,100)
	# plt.figure(1).savefig('SOC', quality=100)
	# plt.grid(True)
	# # Rotating the values along x-axis to 45 degrees
	# # plt.xticks(rotation=15)
	# # plt.tight_layout()	

	return ()

SOC_estimation = SOC_estimation()
