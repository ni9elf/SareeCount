import cv2
import numpy as np

image_path = ''
filename = 'a.jpg'
file = image_path + filename

def display_image(img):
    cv2.imshow('image', img)
    cv2.waitKey(0)
    

# Takes an image, convert it into grayscale, threshold it and makes 
# the darker region white and bright region black and we use morphology 
# close with a rectangular box of (2,8) and then using this image to find
# contours. In images where there is a shelf, there is dark region between
# the two sarees in gray scale image which we use to find seperation 
# between two sarees.
def find_lines2():
	img1 = cv2.imread(file)     
	counter = 0                 
	#display_image(img1)
	gray = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
	th, dst = cv2.threshold(gray, 45, 255, cv2.THRESH_BINARY_INV)
	cv2.imwrite(file[:-4]+"_1.jpg",dst)
	se = np.ones((2, 6), dtype='uint8')
	img = cv2.morphologyEx(dst, cv2.MORPH_CLOSE, se)
	#se = np.ones((3,3), dtype='uint8')
	#img = cv2.dilate(img,se,iterations = 2)
	cv2.imwrite(file[:-4]+"_2.jpg",img)
	#edges = cv2.Canny(img, 100, 200, apertureSize=3)
	#display_image(img)
	im2, contours, hierarchy = cv2.findContours(img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
	total=0
	perimeter = []
	summm = 0
	countt=0
	for i in contours:
		cont = i
		if cv2.arcLength(cont,False) > 100:
			img2 = img1
			a,b,c,d = cv2.boundingRect(cont)
			#print counter
			#print abs(c*d)
			#print cv2.contourArea(cont)
			perimeter.append(cv2.arcLength(cont,False))
			summm = summm + cv2.arcLength(cont,False)
			countt = countt+1
			cv2.drawContours(img2, [cont], -1, (0,255,0), 3)
			#cv2.imwrite("contour"+str(counter)+".png", img2)
			counter = counter + 1
	#display_image(img1)
	cv2.imwrite(file[:-4]+"_3.jpg",img1)
	perimeter.sort()
	avg = (perimeter[countt/2-1] + perimeter[countt/2] + perimeter[countt/2+1]) /3
	print int(summm/avg)
	
	
find_lines2()
