import cv2
vid=cv2.VideoCapture('../video/QRCodeVideo.mp4')
while True:
    success, frame = vid.read()
    if success:
        cv2.imshow('output',frame)
        if cv2.waitKey(1) & 0xFF==ord('q'):
            break
    else:
        break
vid.release()
cv2.destroyAllWindows()
