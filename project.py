#Libraries
import RPi.GPIO as GPIO
import time
import requests
 
#GPIO set Mode
GPIO.setmode(GPIO.BCM)
 
#set GPIO Pins
GPIO_TRIGGER = 18
GPIO_ECHO = 24
 
#set GPIO direction
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)
 
def distance():
# set Trigger to HIGH
	GPIO.output(GPIO_TRIGGER, True)
 
# set Trigger after 0.01ms to LOW
	time.sleep(0.00001)
	GPIO.output(GPIO_TRIGGER, False)
	StartTime = time.time()
	StopTime = time.time()
 
#  StartTime
	while GPIO.input(GPIO_ECHO) == 0:
		StartTime = time.time()
#  StopTime
	while GPIO.input(GPIO_ECHO) == 1:
		StopTime = time.time()
 
# time difference between start and arrival
	TimeElapsed = StopTime - StartTime
# multiply with the sonic speed (34300 cm/s) and divide by 2
	distance = (TimeElapsed * 34300) / 2
    return distance

i = True
while i == True:
	dist = distance()
	if dist <=80:
		print ("Measured Distance = %.1f cm" % dist)
		requests.post('https://maker.ifttt.com/trigger/WithInRange/with/key/dcn2s_hlgJgtrV0gZ4Bu0A')
		i = False
