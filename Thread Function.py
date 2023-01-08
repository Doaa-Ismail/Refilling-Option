#######################################################################################
########## Author  : Doaa Ismail / S-R&D IoT Dep.  #################################### 
########## Date    : 08-Jan-2023                   ####################################
########## Project : General library               ####################################
########## Task    : Thraead Function Test         ####################################
#######################################################################################


#######################################################################################
# Import:
import threading
import time 
from flask import Flask


def print_cube(num):
    # function to print cube of given num
    print("Cube: {}" .format(num * num * num))
 
 
def print_square(num):
    # function to print square of given num
    print("Square: {}" .format(num * num))
 
 #######################################################################################
## Get Api from server once operator entered valid username,password                 ## 
app = Flask(__name__)

@app.route("/refillingmode/api/value=<string:value>")                           # API from Server once validation on Username and Password Done  
def FristApi_(value):
    print('value = ',value)
    return 'ok '+ '[[1,0,2,0,1,2][0,1,2,1,0,2,0,1]]'
    #return render_template("home.html")
    # creating thread
t1 = threading.Thread(target=print_square, args=(10,))
t2 = threading.Thread(target=print_cube, args=(10,))
t3 = threading.Thread(target=lambda: app.run(host="0.0.0.0", port=8080, debug=True, use_reloader=False))
    
    

# starting thread 1
t1.start()
# starting thread 2
t2.start()
# starting thread 3
#t3.start()
       
# wait until thread 1 is completely executed
t1.join()
# wait until thread 2 is completely executed
t2.join()
# wait until thread 3 is completely executed
#t3.join()
# both threads completely executed
print("Done!")

def func1():
    print ('Working 1')
    time.sleep(2)

def func2():
    print ('Working 2')
    time.sleep(10)

if __name__ =="__main__":
    #t1 = threading.Thread(target=func1)
    #t2 = threading.Thread(target=func2)
    # starting thread 1
    #t1.start()
    # starting thread 2
    #t2.start()
    print("before while")
   
    while 1:
        '''# Define the threads and put them in an array
        threads = [
            threading.Thread(target =func1),
            threading.Thread(target = func2)
        ]

        # Func1 and Func2 run in separate threads
        for thread in threads:
            thread.start()
        # Wait until both Func1 and Func2 have finished
        for thread in threads:
            thread.join()'''
       
        # wait until thread 1 is completely executed
        #t1.join()
        # wait until thread 2 is completely executed
        #t2.join()
        '''threads = [
            threading.Thread(target =func1),
            threading.Thread(target = func2)
        ]

        # Func1 and Func2 run in separate threads
        for thread in threads:
            thread.start()
        # Wait until both Func1 and Func2 have finished
        for thread in threads:
            thread.join()'''

        t1 = threading.Thread(target=func1)
        t2 = threading.Thread(target=func2)
        # starting thread 1
        t1.start()
        # wait until thread 1 is completely executed
        t1.join
        # starting thread 2
        t2.start()
        # wait until thread 2 is completely executed
        t2.join()
        time.sleep(1)
        print(0)
        

        
       
        
       
       
        
       


#180Watt , datasheet 550watt
#6.56Kwatt >>>>>>> 6 panal solar 700watt
#440*240cm