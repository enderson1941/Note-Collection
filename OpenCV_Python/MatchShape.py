# MatchShape with Python
import random as rd

import cv2 as cv


def imageprocess1(image):
    processresult = []
    for element in image:
        element = cv.cvtColor(element.copy(), cv.COLOR_BGR2GRAY)
        element = cv.adaptiveThreshold(element, 255,
                                       cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 21, 15)
        processresult.append(element)
    return processresult


def imageprocess2(image, morphsize, morph_iter1, morph_iter2, blur_iter):
    operator_image = image.copy()
    element = cv.getStructuringElement(shape=cv.MORPH_RECT, ksize=(
        morphsize, morphsize), anchor=None)
    cv.morphologyEx(
        operator_image, cv.MORPH_OPEN, kernel=element, dst=operator_image, anchor=None, iterations=morph_iter1)
    cv.morphologyEx(
        operator_image, cv.MORPH_CLOSE, kernel=element, dst=operator_image, anchor=None, iterations=morph_iter2)
    cv.medianBlur(operator_image, blur_iter)
    return operator_image


def MatchShape(pattern_image, inspect_image, threshold_value):
    matchresult = []
    pattern_display = pattern_image.copy()
    result_display = inspect_image.copy()

    image_operator = [pattern_image, inspect_image]
    image_operator = imageprocess1(image_operator)

    image_operator[0] = imageprocess2(image_operator[0], 2, 2, 0, 3)
    image_operator[1] = imageprocess2(image_operator[1], 3, 1, 1, 3)

    image_operator[0], pattern_contour, hierarchy0 = cv.findContours(
        image_operator[0], cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
    # cv.drawContours(pattern_display, pattern_contour, 1, (0,255,0), 3)
    TemplatePattern = pattern_contour[1]
    TemplatePatternLength = cv.arcLength(TemplatePattern, True)
    ##
    inspect_contour = []
    image_operator[1], TempResult, hierarchy1 = cv.findContours(
        image_operator[1], cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
    for contour_var in TempResult:
        length = cv.arcLength(contour_var, True)
        if length > 150 and length < 2000:
            TempValue = cv.matchShapes(TemplatePattern, contour_var,
                                       cv.CONTOURS_MATCH_I2, 0)
            if TempValue < threshold_value:
                color = (rd.randint(0, 255), rd.randint(
                    0, 255), rd.randint(0, 255))
                matchresult.append(TempValue)
                inspect_contour.append(contour_var)
                cv.drawContours(result_display, inspect_contour, -1, color, 3)

    return matchresult, result_display


img1 = cv.imread(
    "D:\\github\\ConsoleApplication2\\temp\\template3_.bmp", cv.IMREAD_COLOR)
img2 = cv.imread(
    "D:\\github\\ConsoleApplication2\\temp\\source.bmp", cv.IMREAD_COLOR)
matchresult, display_image = MatchShape(img1, img2, 0.87)
for value in matchresult:
    print("Inspect Result: ", value)
cv.namedWindow("result", cv.WINDOW_KEEPRATIO)
cv.imshow("result", display_image)

cv.waitKey(-1)
