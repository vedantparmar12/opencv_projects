import cv2
image=cv2.imread('../image/documentscanner2.jpg')
lower=200
higher=400

edge=cv2.Canny(image, lower, higher)
cv2.imshow("opimgae", edge)
cv2.waitKey(0)