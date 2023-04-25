from ultraSound import ORGHCSR04_ULTR
from time import sleep
import wheelmotor

def run_Ultr():
    #front ultr
    Ultr1 = ORGHCSR04_ULTR(25,26)
    #left ultr
    Ultr2 = ORGHCSR04_ULTR(4,36)
    #right ultr
#     Ultr3 = ORGHCSR04_ULTR(23,34)
    Ultr3 = ORGHCSR04_ULTR(12,34)

    while True:
        dist1 = Ultr1.start_scan()
        dist2 = Ultr2.start_scan()
        dist3 = Ultr3.start_scan()
        print("Front %0.2f CM" % dist1, "Left %0.2f CM" % dist2, "Right %0.2f CM" % dist3)
#         print("front Ultr is: %0.2f CM" % dist1)
#         print("left Ultr is: %0.2f CM" % dist2)
#         print("right Ultr is: %0.2f CM" % dist3)
#         print("=====================")
        if dist1 < 15:
            wheelmotor.moveBack()
            sleep(1.5)
            wheelmotor.stop()
        if dist2 < 15:
            wheelmotor.turnRight()
            sleep(1.5)
            wheelmotor.stop()
        if dist3 < 15:
            wheelmotor.turnLeft()
            sleep(1.5)
            wheelmotor.stop()