import cv2
import numpy as np

image_path = '../images/'
filename = 'colorful-indian-and-asian-sari-fabric-in-retail-display-ftaxp2.jpg'
file = image_path + filename


def display_image(img):
    cv2.imshow('image', img)
    cv2.waitKey(0)


def edge_detect():
    img = cv2.imread(file)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 100, 200, apertureSize=3)
    # display_image(img)
    # display_image(edges)
    minLineLength=img.shape[1]-20
    maxLineGap = 1
    #minLineLength = 2500
    maxLineGap = 1
    lines = cv2.HoughLinesP(edges,1,np.pi/180,80,minLineLength,maxLineGap)
    for l in lines:
        for x1,y1,x2,y2 in l:
            cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)
            
    cv2.imwrite('houghlines_ouput.jpg', img)
    display_image(edges)
    display_image(img)


def find_countour():
    img = cv2.imread(file)
    display_image(img)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    th, dst = cv2.threshold(gray, 32, 255, cv2.THRESH_BINARY)
    # dst = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 45, 0)
    #se = np.ones((3, 3), dtype='uint8')
    #dst = cv2.morphologyEx(dst, cv2.MORPH_CLOSE, se)
    edges = cv2.Canny(dst, 100, 200, apertureSize=3)
    display_image(edges)
    cv2.imwrite('countour_output_edge.jpg', edges)
    im2, contours, hierarchy = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # cv2.drawContours(img, contours, -1, (0,255,0), 3)

    for cnt in contours:
        if cv2.contourArea(cnt) < 100:
        # if cv2.arcLength(cnt,True) > 1:
            cv2.drawContours(img, cnt, -1, (0,255,0), 3)

    cnt = contours[5]
    print cv2.contourArea(cnt)
    print cv2.arcLength(cnt,True)
    cv2.imwrite('countour_output.jpg', img)
    display_image(img)


#edge_detect()
find_countour()
