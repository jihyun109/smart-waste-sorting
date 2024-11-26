import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)

GPIO.cleanup()
GPIO.setmode(GPIO.BCM)

servo1_pin = 12
servo2_pin=7

GPIO.setup(servo1_pin, GPIO.OUT)
GPIO.setup(servo2_pin, GPIO.OUT)
servo1 = GPIO.PWM(servo1_pin, 50)
servo2 = GPIO.PWM(servo2_pin, 50)

servo1.start(0)
servo2.start(0)

def set_servo_angle(servo, angle):
    duty_cycle=2+(angle/18)
    servo.ChangeDutyCycle(duty_cycle)
    sleep(0.5)
    servo.ChangeDutyCycle(0)
    
try:
    print("Moving servo1 to 90 degrees")
    set_servo_angle(servo1, 90)
    sleep(1)
    
    print("Moving servo2 to 90 degrees")
    set_servo_angle(servo2, 90)
    sleep(1)
    
    print("Moving servo1 to 45 degrees")
    set_servo_angle(servo1, 45)
    
    sleep(1)
    
    print("Moving servi2 to 135 degrees")
    set_servo_angle(servo2, 135)
    
    sleep(1)
    
finally:
    servo1.stop()
    servo2.stop()
    GPIO.cleanup()
