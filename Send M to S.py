#######################################################################################
########## Author  : Doaa Ismail / S-R&D IoT Dep.  #################################### 
########## Date    : 08-Jan-2023                   ####################################
########## Project : General library               ####################################
########## Task    : Send x to Server Function Test ###################################
#######################################################################################



#######################################################################################
# Import:
from apscheduler.schedulers.background import BackgroundScheduler  ##BlockingScheduler()

from flask import Flask, render_template
import requests
#from requests.exceptions import Timeout
import threading
import time
#######################################################################################


#######################################################################################
def Send_Matrix_To_Server(matrix_of_slots):
    print("Starting Sending : ",matrix_of_slots )
    URL = 'http://192.168.1.3/api'
    try:
        payload= {'row1':str(matrix_of_slots[0]) , 'row2':str(matrix_of_slots[1]), 'row3':str(matrix_of_slots[2]) , 'row4': str(matrix_of_slots[3]) , 'row5': str(matrix_of_slots[4]) ,'row6': str(matrix_of_slots[5])}
        print(payload)
        send_rows = requests.get(URL,payload,timeout=1)
        print(send_rows.status_code)
        if send_rows.status_code == requests.codes.ok:
            print("Sending Done")
        else :
            print("Try Again")

    except requests.RequestException as e:
        print("Server Error Response : ", e)
    except requests.exceptions.ReadTimeout():
        print("Closeing TCP Connection")
    finally:
        print("Function Done")
#######################################################################################


row1 = [0,1,2,0,1,2,0,0]
row2 = [1,1,1,1,2,2,2,2]
row3 = [0,0,0,0,1,1,1,1]
row4 = [1,1,1,1,0,0,0,0]
row5 = [2,2,2,2,2,2,2,2]
row6 = [0,0,0,0,2,2,2,2]

Total_Matrix = []
Total_Matrix.append(row1)
Total_Matrix.append(row2)
Total_Matrix.append(row3)
Total_Matrix.append(row4)
Total_Matrix.append(row5)
Total_Matrix.append(row6)

print(Total_Matrix)

Send_Matrix_To_Server(Total_Matrix)