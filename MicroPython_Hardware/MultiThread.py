import wifi
import ultra_Action
import threading
import time

def loop1():
    wifi.connectWeb()
    
def loop2():
    ultra_Action.run_Ultr()

t1 = threading.Thread(target = loop1)
t2 = threading.Thread(target = loop2)

t1.start()
t2.start()
