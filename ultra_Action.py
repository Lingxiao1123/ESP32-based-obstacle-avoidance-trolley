#import necessary module
from ultraSound import ORGHCSR04_ULTR
import wheelmotor
#uasyncio asynchronous programming library
#allow to run multitasing in one thead with coroutine
import uasyncio
import time

#coroutine function:
async def read_ultr(ultr, delay):
    while True:
        #To make sure it's real time progamming:
        #I recorded the time stamps for the start and end of the mission
        start_time = time.ticks_us()
        dist = ultr.start_scan()
        print("%s: %0.2f CM" % (ultr.name, dist))
        if ultr.name == 'Front' and dist < 20:
            wheelmotor.moveBack()
            await uasyncio.sleep(1.5)
            wheelmotor.stop()
        if ultr.name == 'Left' and dist < 20:
            wheelmotor.turnRight()
            await uasyncio.sleep(1.5)
            wheelmotor.stop()
        if ultr.name == 'Right' and dist < 20:
            wheelmotor.turnLeft()
            await uasyncio.sleep(1.5)
            wheelmotor.stop()
        #elaspsed_time is the total time needed for run this function
        elapsed_time = time.ticks_diff(time.ticks_us(), start_time)
        #if elaspsed_time < delay : we wait for delay_elaspsed_time
        #so that coroutine would be execurte with in delay time
        if elapsed_time < delay:
            await uasyncio.sleep_ms(delay - elapsed_time)
        else:
            await uasyncio.sleep_ms(0)

#in main function, we generate thre Ultrasound object as three task
async def main():
    #front ultr 
    Ultr1 = ORGHCSR04_ULTR(25,26,"Front")
    #left ultr
    Ultr2 = ORGHCSR04_ULTR(4,36,"Left")
    #right ultr
    Ultr3 = ORGHCSR04_ULTR(12,34,"Right")
    #Three corountine tasks with delay time
    #Ultr1 waiting time 100ms , Ultr2 waiting time 200ms , Ultr3 waiting time 300ms
    tasks = [
        read_ultr(Ultr1, 100), 
        read_ultr(Ultr2, 200),  
        read_ultr(Ultr3, 300),  
    ]
    
    await uasyncio.gather(*tasks)

#create event loop
loop = uasyncio.get_event_loop()
loop.create_task(main())
loop.run_forever()

#run mian function
main()
