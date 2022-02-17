import cv2
import uuid   # Unique identifier
import os
import time

IMAGES_PATH = os.path.join('data', 'images')
name_of_file = 'smoke'
# num_of_img = 21

cap = cv2.VideoCapture('videos/stairs-smoke.mp4')
current = 0
frames = 5
while True:
    if frames != 0:
        ret, frame = cap.read()
        frames -= 1
    if frames == 0:
        img_name = os.path.join(IMAGES_PATH, name_of_file+'.'+str(current)+'.jpg')
        cv2.imwrite(img_name, frame)
        current += 1
        frames = 5

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


