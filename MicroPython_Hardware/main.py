import time
import machine
from machine import Pin, Timer

LED_BLINK_TIMER_CLOCK_ms = 1000
timer_period = 1000
led_blink_active_flag = 1
ledstate = 1
timer_interrupt_flag = 1

#right front wheel - good
p18 = Pin(18, Pin.OUT)
p19 = Pin(19, Pin.OUT)
p5 = Pin(5,Pin.OUT)  #p5 - enable
p5.value(1)

#left back wheel - good
p15 = Pin(15, Pin.OUT)
p32 = Pin(32, Pin.OUT)
p14 = Pin(22, Pin.OUT) #p14 - enable
p14.value(1)

#left front wheel - good
p27 = Pin(27,Pin.OUT)
p33 = Pin(33,Pin.OUT)
p22 = Pin(22,Pin.OUT) #p22 - enable
p22.value(1)

#right back wheel - good
p16 = Pin(16,Pin.OUT)
p17 = Pin(17,Pin.OUT)
p21 = Pin(21,Pin.OUT) #p21 - enable
p21.value(1)

def turnLeft():
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

def moveFront():
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

def toggle_led(timer):
    global ledstate
    ledstate = ledstate ^ 1
    if led_blink_active_flag == 1:
        led(ledstate)

def handle_input():  #new functions to handle input values, T,A,B,I
    global timer_period, led_blink_active_flag

    Command = input('')
    if Command == 'T':
        if led_blink_active_flag == 1:
            print("TLED blinking paused \r\n")
        else:
            print("TLED blinking resumed \r\n")
        led_blink_active_flag ^= 1
    elif Command == 'A':
        print('AReceived the A command\r\n')
        timer_period = LED_BLINK_TIMER_CLOCK_ms
        t1.init(period=timer_period, mode=t1.PERIODIC, callback=toggle_led)
    elif Command == 'B':
        print('BReceived the B command\r\n')
        timer_period = timer_period - 100
        if timer_period < 200:
            timer_period = 200
        t1.init(period=timer_period, mode=t1.PERIODIC, callback=toggle_led)
    elif Command == 'L': # car left turn 90 degree
        turnLeft()
        print('LReceived the L command\r\n')
    elif Command == 'R': # car right turn 90 degree
        turnRight()
        print('RReceived the R command\r\n')
    elif Command == 'F': # car going forward a little bit
        moveFront()
        print('FReceived the F command\r\n')
    elif Command == 'C': #trick the cat 
        print('CReceived the C command\r\n')
    elif Command == 'V':
        moveBack()
        print('VReceived the V command\r\n')
    elif Command == 'I':
        print('IESP32\r\n')

led = Pin(13, mode=Pin.OUT)
led(ledstate)
t1 = Timer(1)
t1.init(period=LED_BLINK_TIMER_CLOCK_ms, mode=t1.PERIODIC, callback=toggle_led)
#re-initalize values so ESP32 doesn't reboot itself after typing A and B
print('\r\nESP32 Ready to accept Commands\r\n')

try:
    while True:
        handle_input()
except KeyboardInterrupt:
    t1.deinit()
