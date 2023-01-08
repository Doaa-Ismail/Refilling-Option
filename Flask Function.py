#######################################################################################
########## Author  : Doaa Ismail / S-R&D IoT Dep.  #################################### 
########## Date    : 08-Jan-2023                   ####################################
########## Project : Lpg Vending Machine           ####################################
########## Task    : Refilling Mode by Operator    ####################################
#######################################################################################




#######################################################################################
# Import:
from flask import Flask, render_template
import threading
#######################################################################################


#######################################################################################
## Get Api from server once operator entered valid username,password                 ## 
app = Flask(__name__)

@app.route("/refillingmode/api/value=<string:value>")                           # API from Server once validation on Username and Password Done  
def FristApi_(value):
    print('value = ',value)
    return 'ok '+ '[[1,0,2,0,1,2][0,1,2,1,0,2,0,1]]'
    #return render_template("home.html")

if __name__ == "__main__":
    #app.run(host="0.0.0.0", port=8080, debug=True)
    threading.Thread(target=lambda: app.run(host="0.0.0.0", port=8080, debug=True, use_reloader=False)).start()

'''
data = 'foo'
host_name = "0.0.0.0"
port = 23336
app = Flask(__name__)

@app.route("/")
def main():
    return data

if __name__ == "__main__":
    threading.Thread(target=lambda: app.run(host=host_name, port=port, debug=True, use_reloader=False)).start()

'''


'''

response = requests.post('https://httpbin.org/post', json={'id': 1, 'name': 'Jessa'})

print("Status code: ", response.status_code)
print("Printing Entire Post Request")
print(response.json())

'''


