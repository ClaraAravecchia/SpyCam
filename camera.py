import numpy as np
import cv2 as cv

def main():
    cap = cv.VideoCapture(0)
    if not cap.isOpened():
        print("Cannot open camera")
        exit()
    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()
        # if frame is read correctly ret is True
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break
        
        verify_person(frame)
        # Our operations on the frame come here
        #gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        # Display the resulting frame
        #cv.imshow('frame', frame)
        
        if cv.waitKey(1) == ord('q'):
            break
    # When everything done, release the capture
    cap.release()
    cv.destroyAllWindows()

def verify_person(frame):
    #Verifica se ha uma pessoa naquele frame
    print(frame)
#     body_cascade = cv.CascadeClassifier("/home/pi/Python/opencv/data/haarcascades/haarcascade_fullbody.xml")
    body_cascade = cv.CascadeClassifier("/home/pi/Python/opencv/data/haarcascades/haarcascade_frontalface_default.xml")
    
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    body = body_cascade.detectMultiScale(gray, 1.3, 5)
    
    for(x, y, w, h) in body:
        cv.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        cv.imwrite('/home/pi/frame.jpg', frame)
    cv.imshow('frame', frame)

main()