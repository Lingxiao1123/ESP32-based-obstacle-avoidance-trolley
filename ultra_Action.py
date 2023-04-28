from ultraSound import ORGHCSR04_ULTR
from time import sleep
import wheelmotor
import uasyncio

async def read_ultr(ultr,delay):
    x = []
    y = []
    while True:
        dist = ultr.start_scan()
        print("%s: %0.2f CM" % (ultr.name, dist))
        if ultr.name == 'Front' and dist < 20:
            wheelmotor.moveBack()
            sleep(1.5)
            wheelmotor.stop()
        if ultr.name == 'Left' and dist < 20:
            wheelmotor.turnRight()
            sleep(1.5)
            wheelmotor.stop()
        if ultr.name == 'Right' and dist < 20:
            wheelmotor.turnLeft()
            sleep(1.5)
            wheelmotor.stop()
        await uasyncio.sleep_ms(delay)

def run_Ultr():
    #front ultr
    Ultr1 = ORGHCSR04_ULTR(25,26,"Front")
    #left ultr
    Ultr2 = ORGHCSR04_ULTR(4,36,"Left")
    #right ultr
#     Ultr3 = ORGHCSR04_ULTR(23,34)
    Ultr3 = ORGHCSR04_ULTR(12,34,"Right")
    
    tasks = [
        read_ultr(Ultr1, 100),  # 每 100ms 读取一次前方超声波传感器的距离
        read_ultr(Ultr2, 200),  # 每 200ms 读取一次左侧超声波传感器的距离
        read_ultr(Ultr3, 300),  # 每 300ms 读取一次右侧超声波传感器的距离
    ]
    
    loop = uasyncio.get_event_loop()
    loop.create_task(uasyncio.gather(*tasks))
    loop.run_forever()

#     while True:
#     dist1 = Ultr1.start_scan()
#     dist2 = Ultr2.start_scan()
#     dist3 = Ultr3.start_scan()
#         print("Front %0.2f CM" % dist1, "Left %0.2f CM" % dist2, "Right %0.2f CM" % dist3)
# #         print("front Ultr is: %0.2f CM" % dist1)
# #         print("left Ultr is: %0.2f CM" % dist2)
# #         print("right Ultr is: %0.2f CM" % dist3)
# #         print("=====================")
#         if dist1 < 15:
#             wheelmotor.moveBack()
#             sleep(1.5)
#             wheelmotor.stop()
#         if dist2 < 15:
#             wheelmotor.turnRight()
#             sleep(1.5)
#             wheelmotor.stop()
#         if dist3 < 15:
#             wheelmotor.turnLeft()
#             sleep(1.5)
#             wheelmotor.stop()

run_Ultr()
