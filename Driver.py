from types import NoneType
import serial
import cv2shootcount = 0
vc = cv2.VideoCapture(1)
vc.read()
size = (int(vc.get(cv2.CAP_PROP_FRAME_WIDTH)), int(vc.get(cv2.CAP_PROP_FRAME_HEIGHT)))
fd = cv2.FaceDetectorYN.create("face_detection_yunet_2023mar.onnx","",size)
pico = serial.Serial('COM10', 115200, timeout=1)
while True:
    success, image = vc.read()
    if not success:
        print("Error readxing image")
        break
    success, faces = fd.detect(image)
    if not success:
        print("Error detecting faces")
        break
    if type(faces) != NoneType:
        for face in faces:
            image = cv2.rectangle(image, [int(face[0]), int(face[1]), int(face[2]), int(face[3])], (255, 0, 255))        midpoint = (size[0]/2,size[1]/2)
        delta_x = faces[0][8] - midpoint[0]
        delta_y = faces[0][9] - midpoint[1]
        shoot = False
        if abs(delta_x) < 20:
            x_ratio = 0
            shootcount += 1
        else:
            x_ratio = delta_x / midpoint[0] #Distance from middle as ratio of maximum possible distance
        if abs(delta_y) < 100:
            y_ratio = 0
        else:
            y_ratio = delta_y / midpoint[1]
        if shootcount == 10:
            shoot = True
            shootcount = 0
        pico.write(f"{x_ratio:.3f}\n{y_ratio:.3f}\n{shoot}\n".encode())
        print(x_ratio, y_ratio)
    cv2.imshow("Face detection", image)
    if (cv2.waitKey(5) >= 0):
        break
vc.release()
