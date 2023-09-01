from machine import Pin
import utime
import wheelmotor
from time import sleep

class ORGHCSR04_ULTR:

    def __init__(self,trigNum,echoNum):
        self.trigNum = trigNum
        self.echoNum = echoNum
        self.trig = Pin(trigNum, Pin.OUT)
        self.echo = Pin(echoNum, Pin.IN)
        self.trig.off()
        self.echo.off()

    def start_scan(self): 
#         while True:
            dist = self.start_hc()
#             self.operation(dist)
            utime.sleep_ms(200) # 这里根据需要设定SLEEP时间
            return dist

    def start_hc(self):
        self.trig.on()
        utime.sleep_us(10)
        self.trig.off()

        while self.echo.value() == 0 : 
            pass

        start_us = utime.ticks_us()
        
        while self.echo.value() == 1 : 
            pass

        end_us = utime.ticks_us()
        
        rang_us = utime.ticks_diff(end_us,start_us)/10000

        dist = rang_us*340/2
        
#         print("dist is: %0.2f CM" % dist)
        
        return dist
            
#     def operation(self,dist):
#         while dist < 20:
#             if self.trigNum == 25 and self.echoNum == 26:
#                 wheelmotor.moveBack()
#                 sleep(3)
#                 wheelmotor.stop()
#                 break
#             elif self.trigNum == 4 and self.echoNum == 36:
#                 wheelmotor.turnRight()
#                 sleep(3)
#                 wheelmotor.stop()
#                 break
#             elif self.trigNum == 23 and self.echoNum == 34:
#                 wheelmotor.turnLeft()
#                 sleep(3)
#                 wheelmotor.stop()
#                 break  