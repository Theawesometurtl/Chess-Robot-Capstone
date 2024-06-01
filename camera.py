import cv2


def take_photo():
    
    cam = cv2.VideoCapture(0)
    while True:
        ret, image = cam.read()
        cv2.imshow('Imagetest',image)
        k = cv2.waitKey(1)
        if k != -1:
            cv2.imwrite('/home/pi/testimage.jpg', image)
            cam.release()
            cv2.destroyAllWindows()
