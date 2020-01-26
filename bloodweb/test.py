import cv2
import time
import pyautogui
import numpy as np
from PIL import Image, ImageGrab 

time.sleep(1)
print("start")

# take a screenshot and save it
# 1 inner screenshot
pyautogui.screenshot(("00.png"),region=(527,356,314,348))
# 2 mid screenshot
pyautogui.screenshot(("01.png"),region=(386,222,569,587))
# 3 outer screenshot
pyautogui.screenshot(("02.png"),region=(217,105,976,869))


im = cv2.imread("00.png")
gray_img = cv2.cvtColor(im,	cv2.COLOR_BGR2GRAY)
img	= cv2.medianBlur(gray_img,	5)
cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)


circles	= cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,120,param1=10,param2=40,minRadius=30,maxRadius=44)
circles	= np.uint16(np.around(circles))

count = 1
for	i in circles[0,:]:
    # draw outer circle
    cv2.circle(im,(i[0],i[1]),i[2],(0,255,0),6)
	# draw center circle
    cv2.circle(im,(i[0],i[1]),2,(0,0,255),3)
    # count circles
    cv2.putText(im, "n:" + str(count), (i[0]-65,i[1]+40), cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,255,255),1)
    count += 1


# pyautogui
def mouse(x,y):
    pyautogui.FAILSAFE = True
    pyautogui.moveTo(x=x,y=y,duration=1)
    # pyautogui.PAUSE = 1
    #pyautogui.mouseDown(x=x,y=y,button="left",duration=4)
    # time.sleep(2)
    #pyautogui.mouseUp(x=x,y=y,button="left")

# move the mouse 
for i in range(circles.shape[1]):
    x,y = circles[(0,i,0)], circles[(0,i,1)]
    #print(x,y)
    #mouse(x,y)

number_circles = str(circles.shape[1])
print(number_circles)
print(circles.shape)

cv2.imshow("HoughCirlces", im)
cv2.waitKey()
cv2.destroyAllWindows()

print("end")
