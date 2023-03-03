"""
#!/usr/bin/env python
#title           :Multithread_BMS_Cluster1-5.py
#description     :-
#author          :Fajar Muhammad Noor Rozaqi
#date            :2021/08/09
#version         :0.1
#usage           :BMS-python
#notes           :
#python_version  :3.9
#==============================================================================
"""

#library
import subprocess
import time

#Multithreading
subprocess.Popen(["/usr/bin/python","/home/pi/Desktop/battery_monitoring_cluster_1_raspy.py"])

subprocess.Popen(["/usr/bin/python","/home/pi/Desktop/battery_monitoring_cluster_2_raspy.py"])

subprocess.Popen(["/usr/bin/python","/home/pi/Desktop/battery_monitoring_cluster_3_raspy.py"])

subprocess.Popen(["/usr/bin/python","/home/pi/Desktop/battery_monitoring_cluster_4_raspy.py"])

subprocess.Popen(["/usr/bin/python","/home/pi/Desktop/battery_monitoring_cluster_5_raspy.py"])

#stdout=subprocess.PIPE,stderr=subprocess.PIPE).communicate()
