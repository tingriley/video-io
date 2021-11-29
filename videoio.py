import cv2
JETSON = False
filename = '.mp4'
pipeline = 'filesrc location=%s ! decodebin ! ' % filename

cvt_pipeline = (
                'nvvidconv interpolation-method=5 ! '
                'video/x-raw, format=BGRx !'
                'videoconvert ! appsink sync=false'
            )

stream = pipeline + cvt_pipeline


if JETSON:
    cap = cv2.VideoCapture(stream)
else:
    cap = cv2.VideoCapture(filename)

width  = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height  = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
print(width, height)

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret:
        cv2.imshow("frame", frame)
        cv2.waitKey(1)
    else:
        break

cap.release()
cv2.destroyAllWindows()

