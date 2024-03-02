import cv2
import numpy as np
import time

cap = cv2.VideoCapture('c:\\Users\\Asus\\OneDrive\\Desktop\\output_video_grayscale.avi') 

prev_frame = None
prev_intensity = None
start_time = time.time()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    intensity = np.sum(gray)

    if prev_intensity is not None:
        intensity_diff = abs(intensity - prev_intensity)
        if intensity_diff <=1: 
            print("Intensity change detected at:", time.time() - start_time)

    prev_intensity = intensity

    cv2.imshow('Frame', frame)

    if cv2.waitKey(22) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()