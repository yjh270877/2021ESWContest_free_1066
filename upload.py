import RPi.GPIO as GPIO
import os
import sys
import picamera
import time
import datetime
from gpiozero import Button
from time import sleep        #프로그램 실행에 필요한 라이브러리를 import

def restart():
    os.execl(sys.executable, sys.executable, *sys.argv)   #restart() 변수 생성

start = time.time()          #시작하는 시간 정의
carBreak = Button(17)        #Break를 gpio17번 핀에 연결된 버튼으로 정의
handleLeft = Button(27)      #handleleft를 gpio27번 핀에 연결된 버튼으로 정의
handleRight = Button(22)     #handleright를 gpio22번 핀에 연결된 버튼으로 정의
f = open("upload.txt", "w")  #upload.txt라는 파일만들기

savepath ='./recorded'      #저장경로 지정

camera = picamera.PiCamera()
camera.resolution = (850,480)
camera.start_recording(output = savepath + '/' + 'dondo.h264')     #녹화본 설정

GPIO.setmode(GPIO.BCM) 
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
time.sleep(1)
time_count=0                           #진동센서

while True:
   result = GPIO.input(23)          #진동센서의 결과에 따라              
   if result == 1:
      print("YES")
      sec = time.time()-start
      num = str(sec).split(".")
      num = num[0]
      print(num)
      f.write(num + "sec  : traffic accident detected \n")
      f.close()                        /#upload.txt파일에 시간표기
      camera.stop_recording()          #녹화종료
      os.system('node ./shock.js')     #shock.js 실행
      time.sleep(2)       
      os.system('node ./txt.js')      #txt.js실행
      exit()                       #카메라정상종료
      
   else:
      print("NO")
      time.sleep(1)
      sec = time.time()-start
      times = str(datetime.timedelta(seconds=sec)).split(".")
      times = times[0]
      if carBreak.is_pressed:       #break버튼을 눌렀을 때
          sec = time.time()-start
          num = str(sec).split(".")
          num = num[0]
          print(num + "break")
          f.write(num + "sec  : break motion is detected \n")
      if handleLeft.is_pressed:   #handelleft버튼을 눌렀을 때
          sec = time.time()-start
          num = str(sec).split(".")
          num = num[0]
          print(num + "left")
          f.write(num + "sec  : handle left is detected \n")
      if handleRight.is_pressed:  #handleright버튼을 눌렀을때
          sec = time.time()-start
          num = str(sec).split(".")
          num = num[0]
          print(num + "right")
          f.write(num + "sec  : handle right is detected \n")
      if sec >= 60:      #녹화시간이 60초보다 커지면
          camera.stop_recording()     #녹화종료
          os.system('node ./upload.js')   /#upload.js 실행
          camera.close()
          time.sleep(1)
          restart()     #프로그램 재실행
    
          
    
      
        

          
          
         
