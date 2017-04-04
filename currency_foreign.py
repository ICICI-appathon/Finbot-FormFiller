import numpy as np
import cv2

src=cv2.imread("currency_foreign.png")
img=src.copy()
d_branch="Vikaspuri"
a_branch="Vikaspuri"
a_name="harsh"
a_tel="0000000"
a_mobile="99999999999"
date="23051997"
account_number="000000000000"
print dir(date)
length = len(date)
print length
cv2.putText(img,d_branch,(63,119),cv2.FONT_HERSHEY_SIMPLEX,0.3,(123,123,123),1)
cv2.putText(img,a_branch,(52,136),cv2.FONT_HERSHEY_SIMPLEX,0.3,(123,123,123),1)
cv2.putText(img,a_name,(104,170),cv2.FONT_HERSHEY_SIMPLEX,0.3,(123,123,123),1)
cv2.putText(img,a_mobile,(131,187),cv2.FONT_HERSHEY_SIMPLEX,0.3,(123,123,123),1)
cv2.putText(img,a_tel,(360,187),cv2.FONT_HERSHEY_SIMPLEX,0.3,(123,123,123),1)
i=length-1
j=0
while i > -1 :
	cv2.putText(img,date[i],(386+(i)*14,134),cv2.FONT_HERSHEY_SIMPLEX,0.3,(123,123,123),1)
	i=i-1
i=len(account_number)-1
while i > -1 :
	cv2.putText(img,account_number[i],(329+(i)*14,168),cv2.FONT_HERSHEY_SIMPLEX,0.3,(123,123,123),1)
	i=i-1
cv2.imshow("img",img)
cv2.waitKey(0)
#date (486,134)
#-14