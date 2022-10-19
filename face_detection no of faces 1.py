from cgitb import text
import cv2
video = cv2.VideoCapture(0)
human_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

while True:
    check,frame=video.read()
   
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    
    human = human_cascade.detectMultiScale(gray,1.9,1)
    i=0
    for (x,y,w,h) in human:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
        i=i+1
    
    face='face number'+str(i)
    cv2.putText(frame, face, (x-10, y-10),
                 cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

    cv2.imshow('human_detection',frame)
 
    if cv2.waitKey(1) & 0XFF == ord('q'):
        break
video.release()
cv2.destroyAllWindows()