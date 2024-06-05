import cv2
image=cv2.imread('../image/lambo.png')
imgblur = cv2.GaussianBlur(image, (69,69), 0)
cv2.imshow("opimgae", imgblur)
cv2.waitKey(0)