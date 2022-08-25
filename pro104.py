import cv2
img = cv2.imread("solar-system.jpg")
cv2.imshow("output",img)
print(img)
cv2.imwrite("Solar_systemwithname.jpg",img)
cv2.waitKey(0)

cv2.putText(img,
"Sun",
(20,300),
cv2.FONT_HERSHAY_COMPLEX,
0.5,
(255,255,255)
)

