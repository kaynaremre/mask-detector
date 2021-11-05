

import cv2 
import time
from draw_line import detect_lines
import os

def capture_image():
    video_capture = cv2.VideoCapture(1, cv2.CAP_DSHOW)

    success = True #video_capture.isOpened()

    if(success == False):
        video_capture.open(1)
        success = True
        
    fps = video_capture.get(cv2.CAP_PROP_FPS)
    
    while success: 
        localtime = time.strftime("%Y.%m.%d-%H.%M.%S")
        seconds = int(time.strftime("%S"))
        
        #print(seconds)
        ret, frame = video_capture.read() 
    
        cv2.imshow('frame', frame) 
        if cv2.waitKey(1) & 0xFF == ord('q'): 
            break
        if seconds % 5 == 0:
        #if cv2.waitKey(100) & 0xFF == ord('f'):
            name = localtime+ ".jpg"
            cv2.imwrite(name,frame)
            detect_lines(name)
            if os.path.exists(name):
                os.remove(name)
    video_capture.release()
    cv2.destroyAllWindows() 

capture_image()
