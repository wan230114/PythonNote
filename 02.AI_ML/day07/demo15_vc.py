"""
demo15_vc.py 视频捕获
"""
import cv2 as cv

# 获取视频捕获设备
video_capture = cv.VideoCapture(0)

while True: 
	frame = video_capture.read()[1]
	cv.imshow('frame', frame)
	# 每隔33毫秒自动更新图像
	if cv.waitKey(33) == 27:
		break

video_capture.release()
cv.destroyAllWindows()

