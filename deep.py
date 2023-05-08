from tkinter.filedialog import askopenfilename
import cv2
from deepface import DeepFace


print("""
Hi ! Welcome to MI :)
1)open a file
2)take a picture
""")

choose=input("enter a number: ")

match(choose):
    case "1":
        file = askopenfilename()
        a = DeepFace.analyze(img_path=file,actions=['emotion'])
        print(a[0].get("dominant_emotion"))

    case "2":
        #0: my local computer , "path of video" , or link
        cap=cv2.VideoCapture(0)
        #reading of each frame or picture of video
        ret,frame=cap.read()
        cv2.imshow("photo", frame)
        cv2.imwrite("photo.png", frame)
        a = DeepFace.analyze(frame, actions=['emotion'])
        print(a[0].get("dominant_emotion"))

    case _:
        print("wrong number !")





