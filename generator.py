import threading
import time
import numpy as np
from time import sleep

# @todo T/T_0 parametr

BREATH = False
LOCK = threading.Lock()
HeartIterator = 0
StartTime = time.monotonic()
print("Start: %d " %StartTime)
DATA = []
BreathingData = []

class BreathThread(threading.Thread):
    def run(self):
        file = open("/home/emil/Pulpit/Uczelnia/Mgr/breath.txt", 'w', encoding='utf-8')
        file.write("Time , HeartPhase \n")
        global BREATH
        global StartTime
        global HeartIterator
        while len(DATA) < 10000 :
            #LOCK.acquire()
            BREATH = False
            #LOCK.release()
            sleep(0.01)
            #LOCK.acquire()
            BREATH = True
            file.write(str(time.monotonic() - StartTime)+", " + str(HeartIterator) + "\n")
            BreathingData.append(time.monotonic() - StartTime)
            #LOCK.release()
            print("Breath in \n")
        file.close()




class HeartThread(threading.Thread):
    def run(self):
        file = open("/home/emil/Pulpit/Uczelnia/Mgr/HeartPhase.txt", 'w', encoding='utf-8')
        file.write("Time , Breath, HeartPhase \n")
        global BREATH
        global HeartIterator
        global StartTime
        while len(DATA) < 10000 :
            #LOCK.acquire()
            HeartIterator = 0
            #LOCK.release()
            while HeartIterator < 100 :
                #LOCK.acquire()
                if BREATH :
                    self.responseFunction()
                DATA.append({'time' : time.monotonic() - StartTime, 'breath' : BREATH, 'HeartPhase': HeartIterator})
                file.write(str(time.monotonic() - StartTime)+", " +str(int(BREATH))+", "+ str(HeartIterator) + "\n")
                HeartIterator = HeartIterator + 1
                #LOCK.release()
                sleep(0.00006)
            print("Heartbeat")
        file.close()
        print(DATA)

    def responseFunction(self):
        global HeartIterator
        if HeartIterator < 50 :
            HeartIterator = HeartIterator - HeartIterator/2
            print("Response function delays phase")
            return
        else :
            HeartIterator = HeartIterator + 5
            print("Response function accelerates phase")
            return

def main(arg) :

    a = HeartThread()
    b = BreathThread()
    a.start()
    b.start()

param = 0.02
if __name__ == "__main__":
   main(param)