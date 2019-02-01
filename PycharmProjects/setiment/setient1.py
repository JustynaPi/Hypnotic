import numpy as np
import cv2




face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

cap = cv2.VideoCapture(0)

while 1:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(126, 186, 181),2)    #126, 186, 181   255,0,0
        roi_gray = gray[y:y+h, x:x+w] #i will kill you, work
        roi_color = img[y:y+h, x:x+w]

        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            #cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0, 255, 255),2)
            roi_gray2 = gray[ey:ey+eh, ex:ex+ew]

            for (x_eye,y_eye,w_eye,h_eye) in eyes:
                center = (int(x_eye + 0.5*w_eye), int(y_eye + 0.5*h_eye))
                radius = int(0.5 * (w_eye + h_eye))
                color = (0,0,0)
                thickness = 5
                cv2.circle(roi_color, center, radius, color, thickness)
            for (x_eye,y_eye,w_eye,h_eye) in eyes:
                center = (int(x_eye + 0.5*w_eye), int(y_eye + 0.5*h_eye))
                radius = int(0.4 * (w_eye + h_eye))
                color = (255,255,255)
                thickness = 5
                cv2.circle(roi_color, center, radius, color, thickness)

            for (x_eye,y_eye,w_eye,h_eye) in eyes:
                center = (int(x_eye + 0.5*w_eye), int(y_eye + 0.5*h_eye))
                radius = int(0.3 * (w_eye + h_eye))
                color = (0, 0, 0)
                thickness = 5
                cv2.circle(roi_color, center, radius, color, thickness)
            for (x_eye,y_eye,w_eye,h_eye) in eyes:
                center = (int(x_eye + 0.5*w_eye), int(y_eye + 0.5*h_eye))
                radius = int(0.2 * (w_eye + h_eye))
                color = (255,255,255)
                thickness = 5
                cv2.circle(roi_color, center, radius, color, thickness)
            for (x_eye,y_eye,w_eye,h_eye) in eyes:
                center = (int(x_eye + 0.5*w_eye), int(y_eye + 0.5*h_eye))
                radius = int(0.1 * (w_eye + h_eye))
                color = (0, 0, 0)
                thickness = 3
                cv2.circle(roi_color, center, radius, color, thickness)


    cv2.imshow('img',img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
