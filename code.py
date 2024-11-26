
import RPi.GPIO as GPIO
import time

#GPIO 핀 설정
SERVO1_PIN = 17 # 모터 1번 핀
SERVO2_PIN = 18 # 모터 2번 핀

#GPIO 초기화
GPIO.setmode(GPIO.BCM)
GPIO.setup(SERVO1_PIN,GPIO.OUT)
GPIO.setup(SERVO2_PIN,GPIO.OUT)

# 서보 모터 PWM 설정
servo1 = GPIO.PWM(SERVO1_PIN,50)
servo2 = GPIO.PWM(SERVO2_PIN,50)
servo1.start(0)
servo2.start(0)

def set_servo_angle(servo,angle):
# 서보 모터의 각도를 설정하는 함수
# 각도에 따라 Duty Cycle 계산
duty_cycle = 2 + (angle / 18)
servo.ChangeDutyCycle(duty_cycle)
time.sleep(0.5)
# 모터 움직임 멈춤
servo.ChangeDutyCycle(0)

def classify_waste(waste_type):
# 쓰레기 분류 함수
if waste_type == "paper":
print("종이 감지: 1번 모터 -45도 회전")
# -45도(상대적)
set_servo_angle(servo,45)

elif waste_type == "plastic":
print("플라스틱 감지: 1번 모터 45도 회전")
# 45도 (절대적)
set_servo_angle(servo1, 135)
print("2번 모터는 가만히 둠")

elif waste_type == "can":
print("캔 감지: 1번 모터 45도, 2번 모터 90도 회전")
# 45도(절대적)
set_servo_angle(servo1,135)
# 90도
set_servo_angle(servo2,90)

else:
print("알 수 없는 쓰레기 종류입니다.")
