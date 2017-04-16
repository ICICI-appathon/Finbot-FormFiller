import numpy as np
import cv2

src=cv2.imread("homeform3.png")
img=src.copy()
#
c_id="0000000000011111"
date="23052017"
f_name="HARSH AGRAWAL"
s_name="SHIVAM KOHLI"
t_name="SUKHAD ANAND"
g_name="NIPUN ARORA"
DOB="06041997"
add_f="123,XYZ STREET,VIKASPURI,NEW-DELHI"
pin="110018"
tel="11111111"
mobile="9999999999"
email="win@icici.com"
n_name="VISHRUT KOHLI"
gn_name="NIPUN ARORA"
add_n="456,XYZ STREET,DWARKA,DELHI"
tick="."
a_no="00000000000000"
bank="ICICI"
branch="VIKASPURI"
d_code="000000000"
ifsc="111111111111"
s_tick=tick.decode('utf-8')
length = len(date)
i=length-1
j=0
while i > -1 :
	cv2.putText(img,date[i],(422-j,159),cv2.FONT_HERSHEY_SIMPLEX,0.3,(123,123,123),1)
	i=i-1
	j=j+11
i=length-1
j=0
while i > -1 :
	cv2.putText(img,DOB[i],(238-j,246),cv2.FONT_HERSHEY_SIMPLEX,0.3,(123,123,123),1)
	i=i-1
	j=j+11
i=0
j=0
length=len(f_name)
while i < length :
	cv2.putText(img,f_name[i],(115+j,171),cv2.FONT_HERSHEY_SIMPLEX,0.3,(123,123,123),1)
	i=i+1
	j=j+11
i=0
j=0
length=len(s_name)
while i < length :
	cv2.putText(img,s_name[i],(115+j,201),cv2.FONT_HERSHEY_SIMPLEX,0.3,(123,123,123),1)
	i=i+1
	j=j+11
i=0
j=0
length=len(t_name)
while i < length :
	cv2.putText(img,t_name[i],(115+j,215),cv2.FONT_HERSHEY_SIMPLEX,0.3,(123,123,123),1)
	i=i+1
	j=j+11
i=0
j=0
length=len(g_name)
while i < length :
	cv2.putText(img,g_name[i],(115+j,230),cv2.FONT_HERSHEY_SIMPLEX,0.3,(123,123,123),1)
	i=i+1
	j=j+11
i=0
j=31
k=283
length=len(add_f)
while i < length :
	cv2.putText(img,add_f[i],(j,k),cv2.FONT_HERSHEY_SIMPLEX,0.3,(123,123,123),1)
	i=i+1
	j=j+10
	if(j>213):
		k=k+14;
		j=31;
i=0
j=0
length=len(pin)
while i < length :
	cv2.putText(img,pin[i],(39+j,330),cv2.FONT_HERSHEY_SIMPLEX,0.3,(123,123,123),1)
	i=i+1
	j=j+11
i=0
j=0
length=len(tel)
while i < length :
	cv2.putText(img,tel[i],(139+j,329),cv2.FONT_HERSHEY_SIMPLEX,0.3,(123,123,123),1)
	i=i+1
	j=j+11
i=0
j=0
length=len(mobile)
while i < length :
	cv2.putText(img,mobile[i],(50+j,355),cv2.FONT_HERSHEY_SIMPLEX,0.3,(123,123,123),1)
	i=i+1
	j=j+11
i=0
j=0
length=len(email)
while i < length :
	cv2.putText(img,email[i],(50+j,366),cv2.FONT_HERSHEY_SIMPLEX,0.3,(123,123,123),1)
	i=i+1
	j=j+11
i=0
j=0
length=len(n_name)
while i < length :
	cv2.putText(img,n_name[i],(295+j,282),cv2.FONT_HERSHEY_SIMPLEX,0.3,(123,123,123),1)
	i=i+1
	j=j+11
i=0
j=0
length=len(gn_name)
while i < length :
	cv2.putText(img,gn_name[i],(295+j,297),cv2.FONT_HERSHEY_SIMPLEX,0.3,(123,123,123),1)
	i=i+1
	j=j+11
i=0
j=295
k=312
length=len(add_n)
while i < length :
	cv2.putText(img,add_n[i],(j,k),cv2.FONT_HERSHEY_SIMPLEX,0.3,(123,123,123),1)
	i=i+1
	j=j+10
	if(j>424):
		k=325
		j=242
i=0
j=0
length=len(a_no)
while i < length :
	cv2.putText(img,a_no[i],(63+j,557),cv2.FONT_HERSHEY_SIMPLEX,0.3,(123,123,123),1)
	i=i+1
	j=j+11
i=0
j=0
length=len(bank)
while i < length :
	cv2.putText(img,bank[i],(67+j,570),cv2.FONT_HERSHEY_SIMPLEX,0.3,(123,123,123),1)
	i=i+1
	j=j+11
i=0
j=0
length=len(branch)
while i < length :
	cv2.putText(img,branch[i],(67+j,582),cv2.FONT_HERSHEY_SIMPLEX,0.3,(123,123,123),1)
	i=i+1
	j=j+11
i=0
j=0
length=len(d_code)
while i < length :
	cv2.putText(img,d_code[i],(75+j,592),cv2.FONT_HERSHEY_SIMPLEX,0.3,(123,123,123),1)
	i=i+1
	j=j+11
i=0
j=0
length=len(ifsc)
while i < length :
	cv2.putText(img,ifsc[i],(66+j,612),cv2.FONT_HERSHEY_SIMPLEX,0.3,(123,123,123),1)
	i=i+1
	j=j+11
i=0
j=0
pan="111111111111"
length=len(pan)
while i < length :
	cv2.putText(img,pan[i],(266+j,612),cv2.FONT_HERSHEY_SIMPLEX,0.3,(123,123,123),1)
	i=i+1
	j=j+11
i=0
j=0
pan="111111111111"
length=len(pan)
while i < length :
	cv2.putText(img,pan[i],(227+j,593),cv2.FONT_HERSHEY_SIMPLEX,0.3,(123,123,123),1)
	i=i+1
	j=j+11
i=0
j=0
length=len(c_id)
while i < length :
	cv2.putText(img,c_id[i],(84+j,108),cv2.FONT_HERSHEY_SIMPLEX,0.3,(123,123,123),1)
	i=i+1
	j=j+11
cv2.putText(img,s_tick,(55,545),cv2.FONT_HERSHEY_SIMPLEX,0.8,(123,123,123),5)
cv2.putText(img,s_tick,(30,503),cv2.FONT_HERSHEY_SIMPLEX,0.8,(123,123,123),5)
cv2.putText(img,s_tick,(30,457),cv2.FONT_HERSHEY_SIMPLEX,0.8,(123,123,123),5)
cv2.putText(img,s_tick,(251,545),cv2.FONT_HERSHEY_SIMPLEX,0.8,(123,123,123),5)
cv2.putText(img,s_tick,(187,395),cv2.FONT_HERSHEY_SIMPLEX,0.8,(123,123,123),5)
cv2.imshow("img",img)
cv2.waitKey(0)
#date (486,134)
#-14