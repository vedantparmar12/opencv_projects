import cv2
image=cv2.imread('../image/lambo.png')
imgray= cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('output image', imgray)
cv2.waitKey(0)