import os
import cv2

# cascades: https://github.com/opencv/opencv/tree/master/data/haarcascades
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')


def read_file(image_path):
    if os.path.isfile(image_path):
        img = cv2.imread(image_path)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        return True, img, gray

    else:
        return False, False


while(True):
    input_path = str(input("Enter the path of the file: "))
    val, img, gray = read_file(input_path)
    if val == True:
        break

rects = face_cascade.detectMultiScale(gray, scaleFactor=1.05,
                                            minNeighbors=10, minSize=(30, 30),
                                            flags=cv2.CASCADE_SCALE_IMAGE)


# loop over the bounding boxes
for (x, y, w, h) in rects:
	# draw the face bounding box on the image
	cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)


# show the output image
cv2.imshow("Image", img)
cv2.waitKey(0)
