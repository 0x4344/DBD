import numpy as np
import cv2
from PIL import Image

# im = Image.open("bw.png")#.convert("LA")
# crop = im.crop((315,125,1125,940))
# crop.show()



img = cv2.imread("bw.png",0)
cv2.imshow("bw",img)
cv2.waitKey(0)
cv2.destroyAllWindows()