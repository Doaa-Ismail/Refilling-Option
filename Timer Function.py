#######################################################################################
########## Author  : Doaa Ismail / S-R&D IoT Dep.  #################################### 
########## Date    : 08-Jan-2023                   ####################################
########## Project : General library               ####################################
########## Task    : Timer Function Test           ####################################
#######################################################################################

#######################################################################################
# Import:
from timer import Timer
#from reader import feed
#######################################################################################

def print_cube(num):
    # function to print cube of given num
    print("Cube: {}" .format(num * num * num))


def main():
    """Print the latest tutorial from Real Python"""
    t = Timer()
    t.start()
    print_cube(10)
    #tutorial = feed.get_article(0)
    t.stop()

    #print(t)

if __name__ == "__main__":
    main()