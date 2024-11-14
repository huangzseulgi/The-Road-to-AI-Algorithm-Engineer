#  将每一帧压缩成540p, 对画面进行垂直反转 转为黑白 添加高斯噪声 处理好的每一帧画面保存成一个MP4文件
import cv2
import os
import numpy as np

def add_gaussian_noise(image):
    row, col = image.shape
    mean = 0
    sigma = 15
    gauss = np.random.normal(mean, sigma, (row, col))
    noisy_img = image + gauss
    return noisy_img.astype(np.uint8)

# 设定输入输出文件名
input_video = 'resources/outdoor.mp4'
output_video = 'resources/output.mp4'

# 打开输入视频
cap = cv2.VideoCapture(input_video) 

# 获取视频信息
fps = int(cap.get(cv2.CAP_PROP_FPS))
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# 计算新的帧大小
new_height = 540
new_width = int((new_height / frame_height) * frame_width)

# 创建视频写入对象
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(output_video, fourcc, fps, (new_width, new_height), isColor=False)    

# 处理每一帧
while True:
    ret, frame = cap.read()
    if not ret:
        break   

# 垂直反转
frame = cv2.flip(frame, 0)

# 转为黑白
frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

# 添加高斯噪声
frame = add_gaussian_noise(frame)

# 保存处理后的帧
out.write(frame)    

# 释放资源
cap.release()
out.release()   







