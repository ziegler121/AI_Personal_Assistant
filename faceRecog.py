import cv2
import face_recognition as FR
font=cv2.FONT_HERSHEY_SIMPLEX


#set camera up
width=640
height=360
cam=cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))

jeffFace=FR.load_image_file('C:/Users/Jeff/Desktop/my_stuff/makersplace_stuff/PythonAI/demoImages-master/known/Jeffrey Asiedu.jpeg')
faceLoc=FR.face_locations(jeffFace)[0]
jeffFaceEncode=FR.face_encodings(jeffFace)[0]

knownEncodings=[jeffFaceEncode]
names=['Jeffrey Asiedu']

def recognizeFace():

    while True:
        #instead of reading unknown face from a file, we are reading it from the camera
        ignore,  unknownFace = cam.read()

        unknownFaceRGB=cv2.cvtColor(unknownFace,cv2.COLOR_BGR2RGB)
        faceLocations=FR.face_locations(unknownFaceRGB)
        unknownEncodings=FR.face_encodings(unknownFaceRGB,faceLocations)

        for faceLocation,unknownEncoding in zip(faceLocations,unknownEncodings):
            top,right,bottom,left=faceLocation
            print(faceLocation)
            cv2.rectangle(unknownFace,(left,top),(right,bottom),(255,0,0),3)
            name='Unknown Person'
            matches=FR.compare_faces(knownEncodings,unknownEncoding)
            print(matches)
            if True in matches:
                matchIndex=matches.index(True)
                print(matchIndex)
                print(names[matchIndex])
                name=names[matchIndex]
            cv2.putText(unknownFace,name,(left,top),font,.75,(0,0,255),2)

        cv2.imshow('My Faces',unknownFace)
        if cv2.waitKey(1) & 0xff == ord('q'):
            break
    cam.release()
    cv2.destroyAllWindows()
    return name

    # if name == "Jeffrey Asiedu":
    #     print("Access Granted")
    # else:
    #     print("Access Denied")
    

