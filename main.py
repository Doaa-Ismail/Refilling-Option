#######################################################################################
########## Author  : Doaa Ismail / S-R&D IoT Dep.  #################################### 
########## Date    : 08-Jan-2023                   ####################################
########## Project : Lpg Vending Machine           ####################################
########## Task    : Refilling Mode by Operator    ####################################
#######################################################################################

#######################################################################################
# Description :
# 1- After Validation on Username , Password >>>>>>>>> Send APi from Server 
# 2- Show Map of Matrix and return to DB of server to show in the screen  /// 
# 3- Operator select by buttons on the screen >>>>> button mapped here to number of specific slot  
# 4- Once select button >>>>>> Server Send API number of row and number of button 
# 5- Move motor by info of number of slot  
# 6- open door
# 7- validation by reading of sensor if operator put something or no 
# 8- wait for another selection or close this door and go to another row
#######################################################################################


#######################################################################################
# Import:
from apscheduler.schedulers.background import BackgroundScheduler  ##BlockingScheduler()

from flask import Flask, render_template
import requests
from requests.exceptions import Timeout
import threading
import time
#######################################################################################


#######################################################################################
## Get Api from server once operator entered valid username,password                 ## 
app = Flask(__name__)

@app.route("/refillingmode/api/value=<string:value>")                           # API from Server once validation on Username and Password Done  
def FristApi_(value):
    print('value = ',value)
 
    return 'ok '+ value
    
def flask_function():
    #app.run(host="0.0.0.0", port=8080, debug=True)
    threading.Thread(target=lambda: app.run(host="0.0.0.0", port=8080, debug=True, use_reloader=False)).start()

#######################################################################################



#######################################################################################
def print_t(x):
  print("Background scheduler " + str(x))

#######################################################################################



#######################################################################################
def Send_Matrix_To_Server(matrix_of_slots):
    URL = 'http://192.168.1.3/api'
    try:
        payload= {'row1':str(matrix_of_slots[0]) , 'row2':str(matrix_of_slots[1]), 'row3':str(matrix_of_slots[2]) , 'row4': str(matrix_of_slots[3]) , 'row5': str(matrix_of_slots[4]) ,'row6': str(matrix_of_slots[5])}
        send_rows = requests.get(URL,payload,Timeout=1)
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



#######################################################################################
## Running Flask and Another Function In Background                                  ##
scheduler1 = BackgroundScheduler() #BlockingScheduler()
scheduler2 = BackgroundScheduler() #BlockingScheduler()

scheduler1.add_job(id='Task 1',func=print_t, trigger='interval', args=[1],seconds =2) #will do the print_t work for every 60 seconds

scheduler1.start()

    
scheduler2.add_job(id='Task 2',func=flask_function, trigger='interval',seconds =5) #will do the print_t work for every 60 seconds

scheduler2.start()

#######################################################################################



if __name__ == "__main__":
    #app.run(host="0.0.0.0", port=8080, debug=True)
    #threading.Thread(target=flaskThread).start()
    #flaskThread()

    while 1 :
        time.sleep(0.5)
        print(0)




