from angle_degree.angle_lida import angle
from blink.test_blink import blink
from graphic.graphic_save_eye_life import graphic
from distance.detection_cm import distance

while True:
    graphic()
    try:
        choice = int(input("entry choice go mode >> "))
        # choice = choice.upper()
        if choice == 1:
            print(" >> detection blink")
            blink()
        elif choice == 2:
            print(" >> detection distance")
            distance()
        elif choice == 3:
            print(" >> detection angle")
            angle()
        elif choice == 4:
            print(" >> quit")
            break
        else:
            print(" ** please entry choice go mode **\n")
            pass

    except ValueError as err:
        pass
        print("\n Value error: {0}".format(err))
        print(" ** please entry choice go mode **\n")
# blink()