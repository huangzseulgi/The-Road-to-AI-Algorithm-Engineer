import cv2
import os

video_path = 'resources/piano.mp4'
if not os.path.exists(video_path):
    print("视频文件不存在，请检查路径")
cap = cv2.VideoCapture(video_path)

while True:
    # 读取一帧
    ret, frame = cap.read()  # ret是一个flag来表示是否读取到数据 frame是获取的结果
    # 如果读取数据成功 显示这一帧数据
    if ret:
        cv2.imshow("frame", frame)
    else:
        print("没有读取到数据")
        break

    # 每一帧之间的间隔
    # waitKey(10) & 0xFF == ord('q') 这段代码的作用是等待用户按下键盘上的 'q' 键。
    # waitKey(10) 函数等待用户按键10毫秒，如果用户在10毫秒内按下了 'q' 键，则返回 'q' 键的ASCII码值。
    # & 0xFF 是按位与运算，用于确保我们只考虑ASCII码值的低8位,返回值是32位。
    # ord('q') 返回字符 'q' 的ASCII码值。
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
