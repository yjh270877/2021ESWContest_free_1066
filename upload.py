import RPi.GPIO as GPIO
import os
import sys
import picamera
import time
import datetime
from gpiozero import Button
from time import sleep

def restart():
    os.execl(sys.executable, sys.executable, *sys.argv)

start = time.time()
carBreak = Button(17)
handleLeft = Button(27)
handleRight = Button(22)
f = open("upload.txt", "w")

savepath ='./recorded'

camera = picamera.PiCamera()
camera.resolution = (850,480)
camera.start_recording(output = savepath + '/' + 'dondo.h264')

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
time.sleep(1)
time_count=0

while True:
   result = GPIO.input(23)
   if result == 1:
      print("YES")
      sec = time.time()-start
      num = str(sec).split(".")
      num = num[0]
      print(num)
      f.write(num + "sec  : traffic accident detected \n")
      f.close()
      camera.stop_recording()
      os.system('node ./shock.js')
      time.sleep(2)
      os.system('node ./txt.js')
      exit()
      
   else:
      print("NO")
      time.sleep(1)
      sec = time.time()-start
      times = str(datetime.timedelta(seconds=sec)).split(".")
      times = times[0]
      if carBreak.is_pressed:
          sec = time.time()-start
          num = str(sec).split(".")
          num = num[0]
          print(num + "break")
          f.write(num + "sec  : break motion is detected \n")
      if handleLeft.is_pressed:
          sec = time.time()-start
          num = str(sec).split(".")
          num = num[0]
          print(num + "left")
          f.write(num + "sec  : handle left is detected \n")
      if handleRight.is_pressed:
          sec = time.time()-start
          num = str(sec).split(".")
          num = num[0]
          print(num + "right")
          f.write(num + "sec  : handle right is detected \n")
      if sec >= 300:
          camera.stop_recording()
          os.system('node ./upload.js')
          camera.close()
          time.sleep(1)
          restart()
    
          
    
      
        

          
          
         