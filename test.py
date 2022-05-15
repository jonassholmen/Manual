import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


def BinPick1():
        if GPIO.input(25):
            print('prog1 complete')
            GPIO.output(23, 1)
            print('prog1,1 start')
            sleep(10)
            GPIO.output(23, 0)
        else:
            BinPick1()
                

def BinPick2():
            if GPIO.input(19):
                print('prog2 complete')
                GPIO.output(24, 1)
                sleep(10)
                print('prog2.1 start')
                GPIO.output(24, 0)
            else:
                BinPick2()