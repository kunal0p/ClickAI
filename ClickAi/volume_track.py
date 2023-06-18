import cv2
import time
import numpy as np
import handtracking as htm
import math
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import runpy

wCam,hCam=640,480
cap = cv2.VideoCapture(0)
cap.set(3,wCam)
cap.set(4,hCam)
pTime=0

detector=htm.handDetector(detectionCon=0.7)


devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
#volume.GetMute()
#volume.GetMasterVolumeLevel()
volRange=volume.GetVolumeRange()
minVol=volRange[0]
maxVol=volRange[1]
vol=0
volnb=400
volper=0

while True:
    success, img = cap.read()
    img=detector.findHands(img)
    lmlist=detector.findPosition(img,draw=False)
    if(len(lmlist)!=0):
        #print(lmlist[4],lmlist[8])
        
        x1,y1=lmlist[4][1],lmlist[4][2]
        x2,y2=lmlist[8][1],lmlist[8][2]
        #x3,y3=lmlist[12][1],lmlist[12][2]
        cx,cy=(x1+x2)//2,(y1+y2)//2
        
        cv2.circle(img,(x1,y1),10,(255,0,255),cv2.FILLED)
        cv2.circle(img,(x2,y2),10,(255,0,255),cv2.FILLED)
        cv2.circle(img,(cx,cy),8,(255,0,255),cv2.FILLED)
        cv2.line(img,(x1,y1),(x2,y2),(255,0,255),3)
        
        length=math.hypot(x2-x1,y2-y1)
        #print(length)
        
        vol=np.interp(length,[20,140],[minVol,maxVol])
        volnb=np.interp(length,[20,140],[180,60])
        volper=np.interp(length,[20,140],[0,100])
        print(int(length),vol)
        volume.SetMasterVolumeLevel(vol, None)
        
        
        if(length<22):
            cv2.circle(img,(cx,cy),8,(0,255,0),cv2.FILLED)
        
        cv2.rectangle(img,(50,50),(65,180),(0,255,0),3)
        cv2.rectangle(img,(50,int(volnb)),(65,180),(0,255,0),cv2.FILLED)
        
        
            
        
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img,str(int(fps)), (10, 50), cv2.FONT_HERSHEY_PLAIN, 1,
                    (255, 0, 255), 2)
    cv2.putText(img,f'{int(volper)} %', (10, 210), cv2.FONT_HERSHEY_PLAIN, 1,
                    (0, 255,0), 2)
    
    cv2.imshow("Image", img)
    cv2.waitKey(1)
    
    if(cv2.waitKey(20)==ord('x')):
        cap.release()
        cv2.destroyAllWindows()
        #runpy.run_module("window")
        break