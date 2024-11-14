import cv2

img_path = 'resources/food.png'
image = cv2.imread(img_path)

# 判断图片是否成功加载 若没有则需要报错
if image is None:
    print("Error: Cannot find the image.")
    exit()

# 获取原本图片的数据 宽度高度通道数  shape
print(image.shape)  # 宽度 高度 通道数
height, width = image.shape[:2]

# 将图片的宽度和高度都除以2 将宽度缩减为原来的1/2 需要转化为int类型
new_width = int(width / 2)
new_height = int(height / 2)

# resize图片（包含插值算法）
new_image = cv2.resize(image, (new_width, new_height), interpolation=cv2.INTER_AREA)

# 显示原本的图片和修改之后的图片
cv2.imshow("Original image", image)
cv2.imshow("New image", new_image)

# 关闭窗口
cv2.waitKey(0)
cv2.destroyAllWindows()
