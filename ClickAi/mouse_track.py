import cv2
import numpy as np
import handtrackingmodule as htm
import time
#import autopy
import pyautogui
import runpy

cap=cv2.VideoCapture(0)
wCam,hCam=640,480
frameR=100
smoothning=5
plocx,plocy=0,0
clocx,clocy=0,0
wScr,hScr=pyautogui.size()
#print(wScr,hScr)
cap.set(3,wCam)
cap.set(4,hCam)
pTime=0
detector=htm.handDetector(maxHands=1)

while True:
    success, img = cap.read()
    img=detector.findHands(img)
    lmlist,bbox=detector.findPosition(img,draw=False)
    
    if(len(lmlist)!=0):
        x1,y1=lmlist[8][1:]
        x2,y2=lmlist[12][1:]
        #print(x1,y1,x2,y2)
        
        fingers=detector.fingersUp()
       # print(fingers)
        cv2.rectangle(img,(frameR,frameR),(wCam-frameR,hCam-frameR),(255,0,255),2)
        
        if(fingers[1]==1 and fingers[2]==0 and fingers[4]==0 ):
            x3=np.interp(x1,(frameR,wCam-frameR),(0,wScr))
            y3=np.interp(y1,(frameR,hCam-frameR),(0,hScr))
            
            clocx=plocx+(x3-plocx)/smoothning
            clocy=plocy+(y3-plocy)/smoothning
            
            
            #autopy.mouse.move(wScr-clocx,clocy)
            pyautogui.moveTo(wScr-clocx,clocy)
            cv2.circle(img,(x1,y1),13,(255,0,255),cv2.FILLED)
            plocx,plocy=clocx,clocy
            
        
        if(fingers[1]==1 and fingers[2]==1 and fingers[4]==0):
            length,img,lineinfo=detector.findDistance(8,12,img)
            #print(length)
            if(length<30):
                cv2.circle(img,(lineinfo[4],lineinfo[5]),13,(0,255,0),cv2.FILLED)
                #autopy.mouse.click()
                pyautogui.click()
                
        if(fingers[4]==1 and fingers[1]==1 and fingers[2]==0):
            length,img,lineinfo=detector.findDistance(8,20,img)
            #print(length)
            if(length>=70):
                pyautogui.scroll(80)
            else:
                pyautogui.scroll(-80)
                
        
                  
    
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img,str(int(fps)), (10, 50), cv2.FONT_HERSHEY_PLAIN, 1,
                    (255, 0, 255), 2)
    cv2.imshow("Image", img)
    cv2.waitKey(1)
    
    
    
    if(cv2.waitKey(20)==ord('x')):
        cap.release()
        cv2.destroyAllWindows()
        #runpy.run_module("window")
        break