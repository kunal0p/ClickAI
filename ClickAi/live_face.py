import cv2 as cv

capture= cv.VideoCapture(0)

pretend_mode=cv.CascadeClassifier("face_detector.xml")
while True:
    boolean, frame=capture.read()
    if boolean==True:
        gray=cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
        coordinatelist=pretend_mode.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=3)
        
        for (x,y,w,h) in coordinatelist:
            cv.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
            
        cv.imshow("live face detection",frame)
        
        if(cv.waitKey(20)==ord('x')):
            break

        
capture.release()
cv.destroyAllWindows()