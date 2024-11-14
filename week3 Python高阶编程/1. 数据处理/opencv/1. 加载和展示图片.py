import cv2

img_path ='resources/food.png'

# 以彩色图片读取
img_color = cv2.imread(img_path, cv2.IMREAD_COLOR)
# 以灰度图片读取
img_gray = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)

# 显示图片
cv2.imshow('img_color', img_color)
cv2.imshow('img_gray', img_gray)

# 等待用户按键 然后关闭窗口
cv2.waitKey(0)
cv2.destroyAllWindows()

# 图片缩放
