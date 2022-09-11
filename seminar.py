# Image Acquisition Program 1
# import cv2                    
# img = cv2.imread('lena.png')  ## Read the given image
# cv2.imshow("Output", img)     ## Make Window which shows the output Image
# cv2.waitKey(0)                ## Destroy window if 0 is pressed


## Image Acquisition Program 1 with GRAYSCALE
# import cv2
# img = cv2.imread('lena.png',cv2.IMREAD_GRAYSCALE)  ##IMREAD_GRAYSCALE / IMREAD_COLOR
# cv2.imshow("Output", img)
# cv2.waitKey(0)

# import cv2                    
# img = cv2.imread('lena.png')  

# classNames = []                                              ## take array
# classFile = 'coco.names'                                     ## load file
# with open(classFile, 'rt') as f:                             ## r = read, t = text only
#     classNames = f.read().rstrip('\n').split('\n')           ## rstrip = right strip, split = turn words of string to list

# configPath = 'ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'  ## load config / model
# weightsPath = 'frozen_inference_graph.pb'                    ## load frozen graphs

# net = cv2.dnn_DetectionModel(weightsPath,configPath)         ## create dnn model on given params
# net.setInputSize(320,320)                                    ## height , width
# net.setInputScale(1.0 / 127.5)                               ## To rescale an input in the [0, 255] range to be in the [-1, 1] range, you would pass scale=1./127.5
# net.setInputMean((127.5, 127.5, 127.5))                      ## B , G , R reduced to set I/P Mean
# net.setInputSwapRB(True)                                     ## Swap first and last channel

# classIds, confs, bbox = net.detect(img,confThreshold=0.5)    ## Thresholding = Segmentation

# for classId, confidence, box in zip (classIds.flatten(),confs.flatten(),bbox) : ## Flatten a matrix
#     cv2.rectangle(img,box,color=(0,255,0),thickness = 2)  
#     cv2.putText(img,classNames[classId-1],(box[0]+10,box[0]+30),
#     cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)
#     cv2.putText(img,str(confidence*100),(box[0]+150,box[0]+30),
#     cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)

# cv2.imshow("Output", img)     
# cv2.waitKey(0) 


##Video Capture and Detect
# import cv2                    
# ## img = cv2.imread('robot.jpg')  
# cap = cv2.VideoCapture(0)
# cap.set(4,480)

# classNames = []                                              
# classFile = 'coco.names'                                     
# with open(classFile, 'rt') as f:                            
#     classNames = f.read().rstrip('\n').split('\n')           

# configPath = 'ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'  
# weightsPath = 'frozen_inference_graph.pb'                    

# net = cv2.dnn_DetectionModel(weightsPath,configPath)         
# net.setInputSize(320,320)                                    
# net.setInputScale(1.0 / 127.5)                               
# net.setInputMean((127.5, 127.5, 127.5))                      
# net.setInputSwapRB(True)    
                                 

# while True:
#     success , img = cap.read()   #Capture Frame by Frame (if frame is read correctly success = true)
#     # mask = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
#     classIds, confs, bbox = net.detect(img,confThreshold=0.5)\
    
#     if len(classIds) != 0:    
#         for classId, confidence, box in zip (classIds.flatten(),confs.flatten(),bbox) : 
#             cv2.rectangle(img,box,color=(0,255,0),thickness = 2)  
#             cv2.putText(img,classNames[classId-1],(box[0]+10,box[0]+30),
#             cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)
#             cv2.putText(img,str(confidence*100),(box[0]+150,box[0]+30),
#             cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)
            

#     cv2.imshow("Output", img)
#     # cv2.imshow("Output", mask)     
#     cv2.waitKey(1) 


##Video and PUT Req to Server
# import cv2
# import requests
# import json

# # img = cv2.imread('lena.png')
# cap = cv2.VideoCapture(0)
# cap.set(4,480)
# api_endpoint = 'https://rtr-website-23f62-default-rtdb.firebaseio.com/image/detect/RTR001Grp8312.json'

# content = []
# classNames = []
# classFile = 'coco.names'
# with open(classFile, 'rt') as f:
#     classNames = f.read().rstrip('\n').split('\n')

# configPath = 'ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'
# weightsPath = 'frozen_inference_graph.pb'

# net = cv2.dnn_DetectionModel(weightsPath,configPath)
# net.setInputSize(320,320)
# net.setInputScale(1.0 / 127.5)
# net.setInputMean((127.5, 127.5, 127.5))
# net.setInputSwapRB(True)

# while True:
#     sucess,img = cap.read()
#     classIds, confs, bbox = net.detect(img,confThreshold=0.5)

#     if len(classIds) != 0:
#         for classId, confidence, box in zip (classIds.flatten(),confs.flatten(),bbox) :
#             cv2.rectangle(img,box,color=(0,255,0),thickness = 2)
#             cv2.putText(img,classNames[classId-1],(box[0]+10,box[0]+30),
#             cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)
#             cv2.putText(img,str(confidence*100),(box[0]+150,box[0]+30),
#             cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)

#             value = classNames[classId-1]
#             if value not in content : 
#                 content.append(value)
#                 json_string = json.dumps(content)
#                 print(json_string)
#                 r = requests.put(api_endpoint, data = json_string)

#     cv2.imshow("Output",img)
#     cv2.waitKey(1)