#######################################################################################
########## Author  : Doaa Ismail / S-R&D IoT Dep.  #################################### 
########## Date    : 08-Jan-2023                   ####################################
########## Project : General library               ####################################
########## Task    : Scheduler Function Test       ####################################
#######################################################################################

'''
# Schedule Library imported
import schedule
import time
 
# Functions setup
def sudo_placement():
    print("Get ready for Sudo Placement at Geeksforgeeks")
 
def good_luck():
    print("Good Luck for Test")
 
def work():
    print("Study and work hard")
 
def bedtime():
    print("It is bed time go rest")
     
def geeks():
    print("Shaurya says Geeksforgeeks")
 
# Task scheduling
# After every 10mins geeks() is called.
schedule.every(10).minutes.do(geeks)
 
# After every hour geeks() is called.
schedule.every().hour.do(geeks)
 
# Every day at 12am or 00:00 time bedtime() is called.
schedule.every().day.at("00:00").do(bedtime)
 
# After every 5 to 10mins in between run work()
schedule.every(5).to(10).minutes.do(work)
 
# Every monday good_luck() is called
schedule.every().monday.do(good_luck)
 
# Every tuesday at 18:00 sudo_placement() is called
schedule.every().tuesday.at("18:00").do(sudo_placement)
 
# Loop so that the scheduling task
# keeps on running all time.
while True:
 
    # Checks whether a scheduled task
    # is pending to run or not
    schedule.run_pending()
    time.sleep(1)
'''


#######################################################################################
# Import:
from apscheduler.schedulers.background import BackgroundScheduler  ##BlockingScheduler()
from flask import Flask, render_template

import threading
import time
#######################################################################################


def print_t(x):
  print("Background scheduler " + str(x))


#######################################################################################
## Get Api from server once operator entered valid username,password                 ## 
app = Flask(__name__)

@app.route("/refillingmode/api/value=<string:value>")                           # API from Server once validation on Username and Password Done  
def FristApi_(value):
    print('value = ',value)
    return 'ok '+ '[[1,0,2,0,1,2][0,1,2,1,0,2,0,1]]'
    #return render_template("home.html")

def flask_function():
   t3 = threading.Thread(target=lambda: app.run(host="0.0.0.0", port=8080, debug=True, use_reloader=False)).start()

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
while 1 :
    time.sleep(1)
    print(0)

