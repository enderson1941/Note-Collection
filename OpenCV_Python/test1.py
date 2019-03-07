import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img1 = cv.imread("D:\\github\\Note-Collection\\samplefiles\\lena.jpg")
cv.imshow("test", img1)
cv.waitKey(-1)
