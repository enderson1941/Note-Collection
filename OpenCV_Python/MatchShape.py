# MatchShape with Python
import random as rd
import os
import cv2 as cv

def program_init():
    print("MatchShape Program\nVersion: 1.0")
    print("**************************************************")

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


def parameters_input(code):
    Parameters_ = []
    ret = input(
        "\nPress 'Y/y' to confirm Parameters for image%d, press 'Enter' with default parameters:\n" % code)
    if ret == '':
        if code == 0:
            Parameters_ = [2, 2, 0, 3]
        else:
            Parameters_ = [3, 1, 1, 3]
        return Parameters_
    Parameters_.append(int(input("Set for morphsize:\n")))
    Parameters_.append(int(input("Set for morph_iter1:\n")))
    Parameters_.append(int(input("Set for morph_iter2:\n")))
    Parameters_.append(int(input("Set for blur_iter:\n")))
    return Parameters_


def MatchShape(pattern_image, inspect_image, threshold_value):
    matchresult = []
    pattern_display = pattern_image.copy()
    result_display = inspect_image.copy()

    image_operator = [pattern_image, inspect_image]
    image_operator = imageprocess1(image_operator)
    Parameters_ = parameters_input(0)
    print("Current Parameters applied for pattern image: %d, %d, %d, %d\n" %
          (Parameters_[0], Parameters_[1], Parameters_[2], Parameters_[3]))
    image_operator[0] = imageprocess2(image_operator[0], 2, 2, 0, 3)
    Parameters_ = parameters_input(1)
    print("Current Parameters applied for inspect image: %d, %d, %d, %d\n" %
          (Parameters_[0], Parameters_[1], Parameters_[2], Parameters_[3]))
    image_operator[1] = imageprocess2(image_operator[1], 3, 1, 1, 3)
    input()
    os.system('cls')
    program_init()
    print("\nProgram finished.\n")
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
                cv.drawContours(result_display, inspect_contour, -1, color, 6)

    return matchresult, result_display


# Main programs
program_init()
path1 = input("\nInput absolute or relative path for Pattern Image:\n")
if path1 == '':
    print("Input path is invalid!")
    exit()
path2 = input("\nInput absolute or relative path for Inspect Image:\n")
if path2 == '':
    print("Input path is invalid!")
    exit()
img1 = cv.imread(path1, cv.IMREAD_COLOR)
# "D:\\github\\Note-Collection\\samplefiles\\template3_.bmp"
img2 = cv.imread(path2, cv.IMREAD_COLOR)
# "D:\\github\\Note-Collection\\samplefiles\\source.bmp"
if img1 is None or img2 is None:
    print("Input image is invalid!")
    exit()
threshold_ = input("\nInput threshold value for Inspection:\n")
if float(threshold_) <= 0:
    print("Input threshold is below zero!")
    exit()
matchresult, display_image = MatchShape(img1, img2, float(threshold_))
for value in matchresult:
    print("Inspect Result: %.4f" % value)
print("\n**************************************************")
cv.namedWindow("result", cv.WINDOW_KEEPRATIO)
cv.imshow("result", display_image)

cv.waitKey(-1)
