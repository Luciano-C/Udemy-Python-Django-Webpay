import cv2

img = cv2.imread("black-hole.jpg")
cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

