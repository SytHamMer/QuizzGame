import time
from datetime import datetime as dt

#This class will start a timer at the moment the object is create ! 

class Timer: 

    def __init__(self,duration):
        """IN: Duration is the duration of the timer in SECONDS"""
        self.start = int(time.time())
        self.timing = duration

    def end(self):
        return(int(time.time())- self.start)>self.timing

    def getTime(self):
        """OUT: 
        A tuple:
        [0] : if timer is finish or not
        [1] : time left, since the begining of the timer"""
        timeleft = self.timing - (int(time.time()) - self.start)
        res =(timeleft,True)
        if timeleft<0:
            res = (timeleft,False)
        return res

 

################ TEST ZONE############
if __name__ == "__main__":
    print(int(time.time()))
    test = Timer(10)
    time.sleep(2)
    print(test.getTime())
    time.sleep(3)
    print(test.getTime())
    time.sleep(2)
    print(test.getTime())