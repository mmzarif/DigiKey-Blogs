#find index of camera in the list of cameras
import cv2

# Get the list of available cameras
def get_camera_list():
    camera_list = []
    for i in range(10):  # Check first 10 indices for cameras
        cap = cv2.VideoCapture(i)
        if cap.isOpened():
            camera_list.append(i)
            cap.release()
    return camera_list

