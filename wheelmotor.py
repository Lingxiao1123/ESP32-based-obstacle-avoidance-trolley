from machine import Pin
import time

#trick the cat motor
p12 = Pin(12,Pin.OUT)
p13 = Pin(13,Pin.OUT)

#right front wheel - good
p18 = Pin(18, Pin.OUT)
p19 = Pin(19, Pin.OUT)
p5 = Pin(5,Pin.OUT)
# p5.value(1)

#left back wheel - good
p15 = Pin(15, Pin.OUT)
p32 = Pin(32, Pin.OUT)
p14 = Pin(22, Pin.OUT)
# p14.value(1)

#left front wheel - good
p27 = Pin(27,Pin.OUT)
p33 = Pin(33,Pin.OUT)
p22 = Pin(22,Pin.OUT)
# p22.value(1)


#right back wheel - good
p16 = Pin(16,Pin.OUT)
p17 = Pin(17,Pin.OUT)
p21 = Pin(21,Pin.OUT)
# p21.value(1)

def Enable():
    p13.value(1)
    p14.value(1)
    p5.value(1)
    p21.value(1)
    

def moveFront():
    Enable()
    #move forward right front;
    p18.value(0)
    p19.value(1)
    #move forward left back;
    p15.value(1)
    p32.value(0)
    #move forward left front;
    p27.value(0)
    p33.value(1)
    #move forware right back;
    p16.value(1)
    p17.value(0)

def moveBack():
    Enable()
    #move backward right front;
    p18.value(1)
    p19.value(0)
    #move backward left back;
    p15.value(0)
    p32.value(1)
    #move backward left front;
    p27.value(1)
    p33.value(0)
    #move backware right back;
    p16.value(0)
    p17.value(1)

def turnLeft():
    Enable()
    #move forward right front;
    p18.value(0)
    p19.value(1)
    #move forware right back;
    p16.value(1)
    p17.value(0)
    #move backward left back;
    p15.value(0)
    p32.value(1)
    #move backward left front;
    p27.value(1)
    p33.value(0)

def turnRight():
    Enable()
    #move backward right front;
    p18.value(1)
    p19.value(0)   
    #move backware right back;
    p16.value(0)
    p17.value(1)
    #move forward left back;
    p15.value(1)
    p32.value(0)
    #move forward left front;
    p27.value(0)
    p33.value(1)

def stop():
    p18.value(0)
    p19.value(0)
    p15.value(0)
    p32.value(0)
    p27.value(0)
    p33.value(0)
    p16.value(0)
    p17.value(0)
    p21.value(0)

#test
# moveFront()
# time.sleep(2)
# moveBack()
# time.sleep(2)
# turnLeft()
# time.sleep(2)
# turnRight()
# time.sleep(2)

stop()


    

    
