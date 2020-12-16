import numpy as np
import cv2
import dlib
#
# def ImageFaceRecognition():
#     #read image
#     img = cv2.imread("human.JPG")
#
#     #RGB --> GRAY
#     gray = cv2.cvtColor(src=img, code=cv2.COLOR_BGR2GRAY)
#
#     #load face recognition detector from dlib
#     face_detector = dlib.get_frontal_face_detector()
#
#     #predictor load
#     predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
#
#     #find faces
#     faces = face_detector(gray)
#
#     #draw square in img
#     for face in faces:
#         x1 = face.left()
#         y1 = face.top()
#         x2 = face.right()
#         y2 = face.bottom()
#
#         cv2.rectangle(img=img, pt1=(x1,y1), pt2=(x2,y2), color=(0,255,0), thickness=3)
#
#         face_feature = predictor(image=gray, box=face)
#         for n in range(0, 68):
#             x = face_feature.part(n).x
#             y = face_feature.part(n).y
#             cv2.circle(img=img, center=(x,y), radius=2, color=(0,0,255), thickness=1)
#
#     cv2.imshow(winname="Face Recognition", mat=img)
#     cv2.waitKey(delay=0)
#     cv2.destroyAllWindows()
def CameraFaceRecognition():
	# face_detector = cv2.CascadeClassifier('src/cascades/data/haarcascade_frontalface_alt2.xml')
	face_detector = dlib.get_frontal_face_detector()
	vid = cv2.VideoCapture(0)
	while(True):

			# Capture the video frame
			# by frame
		ret, frame = vid.read()
		gray = cv2.cvtColor(src=frame, code=cv2.COLOR_BGR2GRAY)
		# predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
		# faces = face_detector.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)
		faces = face_detector(gray)
		for face in faces:
			# print(x,y,w,h)
			# roi_gray = gray[y:y+h, x:x+w]
			# roi_color = frame[y:y+h, x:x+w]
			# img_item = "my-image.png"
			# cv2.imwrite(img_item, roi_gray)
			color = (0,255,0)
			stroke = 2
			# width= x + w
			# heigh = y + h

			x1 = face.left()
			y1 = face.top()
			x2 = face.right()
			y2 = face.bottom()

			font = cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
			cv2.putText(frame, 'Person', (x1,y1), font, 1, color, stroke, cv2.LINE_AA)
			# cv2.rectangle(img=frame, pt1=(x,y), pt2=(width,heigh), color=color, thickness=stroke)
			cv2.rectangle(img=frame, pt1=(x1,y1), pt2=(x2,y2), color=color, thickness=stroke)

		cv2.imshow(winname="Face Recognition", mat=frame)

		if cv2.waitKey(20) & 0xFF == ord('q'):
				break

	vid.release()
	cv2.destroyAllWindows()

def main():
    CameraFaceRecognition()

if __name__ == "__main__":
    main()
