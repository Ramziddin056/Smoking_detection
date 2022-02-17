# import cv2
# import numpy as np
# import torch
#
# model = torch.hub.load('ultralytics/yolov5', 'custom', path='stairs-smoke.pt', force_reload=True)
#
# cap = cv2.VideoCapture(0)
# while cap.isOpened():
#     ret, frame = cap.read()
#
#     # Make detections
#     results = model(frame)
#
#     cv2.imshow('YOLO', np.squeeze(results.render()))
#
#     if cv2.waitKey(10) & 0xFF == ord('q'):
#         break
# cap.release()
# cv2.destroyAllWindows()