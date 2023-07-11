import cv2
image = cv2.imread("img2.jpg")
grey__img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
inv = cv2.bitwise_not(grey__img)
blur = cv2.GaussianBlur(inv, (21,21),0)
invBlur = cv2.bitwise_not(blur)
sketch = cv2.divide(grey__img, invBlur, scale=256.0)
cv2.imwrite("FinalResult1.png", sketch)