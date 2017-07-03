import sys
sys.path.append('/usr/local/lib/python2.7/site-packages')
import numpy as np
import cv2
src=cv2.imread("SBI.jpg")
img=src.copy()
account_no="0000000000011111"
cv2.putText(img,account_no,(52,85),cv2.FONT_HERSHEY_SIMPLEX,0.4,(123,123,123),1)
cv2.putText(img,account_no,(542,85),cv2.FONT_HERSHEY_SIMPLEX,0.4,(123,123,123),1)
cv2.putText(img,account_no,(202,225),cv2.FONT_HERSHEY_SIMPLEX,0.4,(123,123,123),1)
cv2.putText(img,account_no,(202,251),cv2.FONT_HERSHEY_SIMPLEX,0.4,(123,123,123),1)
cv2.putText(img,account_no,(202,85),cv2.FONT_HERSHEY_SIMPLEX,0.4,(123,123,123),1)

cv2.putText(img,account_no,(218,323),cv2.FONT_HERSHEY_SIMPLEX,0.4,(123,123,123),1)
cv2.putText(img,account_no,(222,349),cv2.FONT_HERSHEY_SIMPLEX,0.4,(123,123,123),1)
cv2.putText(img,account_no,(168,375),cv2.FONT_HERSHEY_SIMPLEX,0.4,(123,123,123),1)
cv2.putText(img,account_no,(170,400),cv2.FONT_HERSHEY_SIMPLEX,0.4,(123,123,123),1)
cv2.putText(img,account_no,(187,424),cv2.FONT_HERSHEY_SIMPLEX,0.4,(123,123,123),1)
cv2.putText(img,account_no,(333,455),cv2.FONT_HERSHEY_SIMPLEX,0.4,(123,123,123),1)
cv2.putText(img,account_no,(333,481),cv2.FONT_HERSHEY_SIMPLEX,0.4,(123,123,123),1)
cv2.putText(img,account_no,(333,507),cv2.FONT_HERSHEY_SIMPLEX,0.4,(123,123,123),1)
cv2.putText(img,account_no,(287,548),cv2.FONT_HERSHEY_SIMPLEX,0.4,(123,123,123),1)
cv2.putText(img,account_no,(467,548),cv2.FONT_HERSHEY_SIMPLEX,0.4,(123,123,123),1)
cv2.putText(img,account_no,(177,548),cv2.FONT_HERSHEY_SIMPLEX,0.4,(123,123,123),1)
cv2.putText(img,account_no,(122,588),cv2.FONT_HERSHEY_SIMPLEX,0.4,(123,123,123),1)
#cv2.rectangle(img,(230,367),(427,352),(0,0,255),2)
#cv2.rectangle(img,(230,346),(425,331),(255,0,0),2)
cv2.imshow("img",img)
cv2.waitKey(0)
#date (486,134)
#-14
