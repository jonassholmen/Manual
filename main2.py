from flask import Flask, request
from flask_cors import cross_origin
from test import *
from time import sleep


app = Flask(__name__)
GPIO.setup(6,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)
GPIO.setup(24,GPIO.OUT)
GPIO.setup(19,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(20,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(25,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.output(6, 0)
GPIO.output(23, 0)
GPIO.output(24, 0)

sleep(10)


@app.route('/post', methods=['POST'])
# Dette er config slik at du tillater at en uidentifisert aktør bruker endepunktet
@cross_origin(origin='*',headers=['Content- Type','Authorization'])
def hello_world():
    # Her henter du ut body'en
    # Getting information from body
    content = request.json

    # Values from order
    num = int(content["verdi1"]) # Value 1 (Circle)
    num2 = int(content["verdi2"]) # Value 2 (Brick)


    if num == 0:
        if num2 == 0:
            return "ok"


    #Presets
    GPIO.output(23, 0)
    GPIO.output(24, 0)
    GPIO.output(6, 0)

    GPIO.output(6, 1)
    
    while GPIO.input(20) == 0:
                sleep(1)
    GPIO.output(6,0)
    #Circle program if ordered
    if num > 0:
        GPIO.output(23, 1)
        sleep(10)
        GPIO.output(23, 0)
        for i in range(1,num):
            while GPIO.input(25) == 0:
                GPIO.output(23,0)
                sleep(1)
            BinPick1()
    else:
        GPIO.output(23, 0)


    #Brick program if ordered
    if num2 > 0:
        if num > 0:
            while GPIO.input(25) == 0:
                GPIO.output(24,0)
                sleep(1)
        GPIO.output(24, 1)
        sleep(10)
        GPIO.output(24, 0)
        for i in range(1,num2):
            while GPIO.input(19) == 0:
                GPIO.output(24,0)
                sleep(1)
            BinPick2()
    else:
        GPIO.output(24, 0)
    

    #Initiating start of MiR
    if num2 > 0:
            while GPIO.input(19) == 0:
                sleep(1)
            GPIO.output(6,1)
            sleep(3)
            GPIO.output(6,0)
    elif num > 0:
            while GPIO.input(25) == 0:
                sleep(1)
            GPIO.output(6,1)
            sleep(3)
            GPIO.output(6,0)
            
    # Simple return to prevent crash
    return "ok"


if __name__ == '__main__':
    app.run(debug=False, port=5001, host='192.168.1.158')

