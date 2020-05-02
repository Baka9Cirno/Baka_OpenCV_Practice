import cv2 as cv
import time


filename = "F:\\Videos\\幻想万华镜\\01.mp4"

cap = cv.VideoCapture()
if cap.open(filename, cv.CAP_ANY):
    print("Succeed in opening the video file.")
else:
    print("Failed in opening the video file.")
    exit()

time1 = time.time()

bgr = [None] * 3

FPS = cap.get(cv.CAP_PROP_FPS)

width = 0
height = 0
centralCol = 0
centralRow = 0
#width = frame.shape(1)
#height = frame.shape(0)
width = cap.get(cv.CAP_PROP_FRAME_WIDTH)
height = cap.get(cv.CAP_PROP_FRAME_HEIGHT)
centralCol = (width - 1) / 2
centralRow = (height - 1) / 2

#使用函数flip进行翻转, 不用手动翻转

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    srcImage = frame[0:int(centralRow) + 1, 0:int(centralCol) + 1]  #最后一个元素index不包含
    horizental = cv.flip(srcImage, 1, dst = None)
    vertical = cv.flip(srcImage, 0, dst = None)
    both = cv.flip(srcImage, -1, dst = None)

    frame[0:int(centralRow)+1, int(centralCol)+1:int(width)] = horizental
    frame[int(centralRow)+1:int(height), 0:int(centralCol+1)] = vertical
    frame[int(centralRow)+1:int(height), int(centralCol)+1:int(width)] = both
    
    
    cv.imshow("Flipped", frame)
    if cv.waitKey(1) == ord("q") or not cv.getWindowProperty("Flipped", cv.WND_PROP_VISIBLE):
        print("Manually Aborted!")
        break

time2 = time.time()
    
cv.destroyAllWindows()
print("Finished in " + str(time2 - time1) + " S")
