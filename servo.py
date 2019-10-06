
import RPi.GPIO as GPIO
import time
from numpy import arange

servo_180 = 22
servo_30 = 11
kanon = 8
GPIO.setmode(GPIO.BOARD)
GPIO.setup(servo_180, GPIO.OUT)
GPIO.setup(servo_30, GPIO.OUT)
GPIO.setup(kanon, GPIO.OUT)
pwm = GPIO.PWM(servo_180, 50)
ser30 = GPIO.PWM(servo_30, 50)

pwm.start(0)
ser30.start(0)
try:
    while True:
        for i in arange(3.0,8.0,0.5):
            pwm.ChangeDutyCycle(i)
            time.sleep(.5)
            #print("i = ",i)


        for x in range(3,5):
            ser30.ChangeDutyCycle(x)

            #print("x = ",x)

            GPIO.output(kanon,GPIO.HIGH)
            #print("LED ON")
            time.sleep(1)
        for x in range(5,3,-1):
            ser30.ChangeDutyCycle(x)
            #print("x = ",x)
            GPIO.output(kanon,GPIO.LOW)
            #print("LED OFF")
            time.sleep(1)


        for i in arange(7.5,12.0,0.5):
            pwm.ChangeDutyCycle(i)
            time.sleep(.5)
            #print("i = ",i)


        for i in arange(12.0,7.0,-0.5):
            pwm.ChangeDutyCycle(i)
            time.sleep(.5)
            #print("i = ",i)


        for x in range(3,5):
            ser30.ChangeDutyCycle(x)
            #print("x = ",x)
            GPIO.output(kanon,GPIO.HIGH)
            #print("LED ON")
            time.sleep(1)
        for x in range(5,3,-1):
            ser30.ChangeDutyCycle(x)
            #print("x = ",x)

            GPIO.output(kanon,GPIO.LOW)
            #print("LED OFF")
            time.sleep(1)
        for i in arange(7.5,3.0,-0.5):

            pwm.ChangeDutyCycle(i)
            time.sleep(.5)
            #print("i = ",i)

except KeyboardInterrupt:
    pwm.stop()
    ser30.stop()
    GPIO.cleanup()
