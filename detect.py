import cv2
import requests
import json

# img = cv2.imread('lena.png')
cap = cv2.VideoCapture(0)
cap.set(4,480)
api_endpoint = 'https://rtr-website-23f62-default-rtdb.firebaseio.com/image/detect/RTR001Grp8312.json'

content = []
classNames = []
classFile = 'coco.names'
with open(classFile, 'rt') as f:
    classNames = f.read().rstrip('\n').split('\n')

configPath = 'ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'
weightsPath = 'frozen_inference_graph.pb'

net = cv2.dnn_DetectionModel(weightsPath,configPath)
net.setInputSize(320,320)
net.setInputScale(1.0 / 127.5)
net.setInputMean((127.5, 127.5, 127.5))
net.setInputSwapRB(True)

while True:
    sucess,img = cap.read()
    classIds, confs, bbox = net.detect(img,confThreshold=0.5)

    if len(classIds) != 0:
        for classId, confidence, box in zip (classIds.flatten(),confs.flatten(),bbox) :
            cv2.rectangle(img,box,color=(0,255,0),thickness = 2)
            cv2.putText(img,classNames[classId-1],(box[0]+10,box[0]+30),
            cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)
            cv2.putText(img,str(confidence*100),(box[0]+150,box[0]+30),
            cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)

            value = classNames[classId-1]
            if value not in content : 
                content.append(value)
                json_string = json.dumps(content)
                print(json_string)
                r = requests.put(api_endpoint, data = json_string)

    cv2.imshow("Output",img)
    cv2.waitKey(1)