import numpy as np
import cv2

src=cv2.imread("SBIform.png")
img=src.copy()
#
account_no="0000000000011111"
s_tick=tick.decode('utf-8')
length = len(date)
i=length-1
j=0
#cv2.putText(img,account,(422-j,159),cv2.FONT_HERSHEY_SIMPLEX,0.3,(123,123,123),1)
#cv2.putText(img,DOB,(238-j,246),cv2.FONT_HERSHEY_SIMPLEX,0.3,(123,123,123),1)
#cv2.putText(img,f_name[i],(115+j,171),cv2.FONT_HERSHEY_SIMPLEX,0.3,(123,123,123),1)
#cv2.putText(img,s_name[i],(115+j,201),cv2.FONT_HERSHEY_SIMPLEX,0.3,(123,123,123),1)
#cv2.putText(img,t_name[i],(115+j,215),cv2.FONT_HERSHEY_SIMPLEX,0.3,(123,123,123),1)
#cv2.putText(img,g_name[i],(115+j,230),cv2.FONT_HERSHEY_SIMPLEX,0.3,(123,123,123),1)
#cv2.putText(img,add_f[i],(j,k),cv2.FONT_HERSHEY_SIMPLEX,0.3,(123,123,123),1)
#cv2.putText(img,s_tick,(55,545),cv2.FONT_HERSHEY_SIMPLEX,0.8,(123,123,123),5)
#cv2.putText(img,s_tick,(30,503),cv2.FONT_HERSHEY_SIMPLEX,0.8,(123,123,123),5)
#cv2.putText(img,s_tick,(30,457),cv2.FONT_HERSHEY_SIMPLEX,0.8,(123,123,123),5)
#cv2.putText(img,s_tick,(251,545),cv2.FONT_HERSHEY_SIMPLEX,0.8,(123,123,123),5)
#cv2.putText(img,s_tick,(187,395),cv2.FONT_HERSHEY_SIMPLEX,0.8,(123,123,123),5)
#cv2.rectangle(img,(230,367),(427,352),(0,0,255),2)
#cv2.rectangle(img,(230,346),(425,331),(255,0,0),2)
cv2.imshow("img",img)
cv2.waitKey(0)
#date (486,134)
#-14
