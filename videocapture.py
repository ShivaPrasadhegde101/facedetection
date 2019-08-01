import cv2,time



face_cascade = cv2.CascadeClassifier("C:\\Users\\MAHE\\Desktop\\python\\opencv\\opencv-master\\data\\haarcascades\\haarcascade_frontalface_default.xml")

video=cv2.VideoCapture(0)

check,frame=video.read()

greyscale=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(greyscale,1.05,5)

for x,y,w,z in faces:
    frame=cv2.rectangle(frame,(x,y),(x+w,y+z),(255,0,0),2)

cv2.imshow('Image',frame)

cv2.waitKey(0)
time.sleep(3)

video.release()

