import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)         # 오류 무시
GPIO.setmode(GPIO.BCM)          # GPIO BCM 모드 설정

LED = 21 # BCM P21

GPIO.setup(LED, GPIO.OUT)

while 1:                        # 무한 반복 - LED On/Off

    GPIO.output(LED, GPIO.HIGH) 
    time.sleep(0.5)

    GPIO.output(LED, GPIO.LOW)
    time.sleep(0.5)
