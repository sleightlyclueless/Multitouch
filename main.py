import cv2
from Blob import Blob
from Tracker import Tracker
from MyTuioServer import MyTuioServer

# GLOBALS IMAGE PROCESS
_BlurHighPass:int = 15 # first opening & closing (the higher the MORE of the image remains)
_BlurSmoothing:int = 6 # second opening & closing (the higher the LESS of the image remains)
_Threshold:int = 10  # pixels above x/255 greyscale value will be taken as clot parts
_ContourThreshold:int = 8  # pixel clots above this size will be circled

# GLOBALS TRACKER
_maxDistance:int = 25

# P1 processing + P2 Bloblist initializing
def processImage(background, frame):
    # get first diffImage between blank background and current pixel set
    diffImage = cv2.absdiff(background, frame)
    # blur the image to further thin out background of hand
    blurImage = cv2.blur(diffImage, (_BlurHighPass, _BlurHighPass))

    # extract difference between blurred thinned image and pixel difference
    diffImage2 = cv2.absdiff(blurImage, diffImage)
    # blur it a little more to ged rid of more remaining blobs
    blurImage2 = cv2.blur(diffImage2, (_BlurSmoothing, _BlurSmoothing))
    # --> Just the blobs of most contact (fingers) remain

    # turn to greyscale image and just get the best contacts of threshold of 10/255 and more (very low?)
    grayImage = cv2.cvtColor(blurImage2, cv2.COLOR_BGR2GRAY)
    ret, thresholdImage = cv2.threshold(grayImage, _Threshold, 255, cv2.THRESH_BINARY)  # returns two values!
    cv2.imshow("THRESHOLD", thresholdImage)

    # pythify the c++ opencv function given: draw ellipse
    contours, hierarchy = cv2.findContours(thresholdImage, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)
    
    foundBlobs = []

    if hierarchy is not None:
        for idx in range(len(hierarchy[0])):
            if cv2.contourArea(contours[idx]) > _ContourThreshold and len(contours[idx]) >= 4:
                if len(contours[idx]) >= 5:
                    cv2.ellipse(frame, cv2.fitEllipse(contours[idx]), (0, 0, 255))
                    cv2.drawContours(frame, contours, idx, (255, 0, 0), hierarchy=hierarchy)

                    moments = cv2.moments(contours[idx])
                    blob = Blob((int)(moments["m10"]/moments["m00"]), (int)(moments["m01"]/moments["m00"]))
                    foundBlobs.append(blob)

    return foundBlobs

# # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # MAIN # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # #
# VIDEO SOURCE
# cap = cv2.VideoCapture(0) # WEBCAM
cap = cv2.VideoCapture("mt_camera_raw.AVI")

# TRACKER
tracker = Tracker(_maxDistance)


# IF VIDEO FOUND
if cap:
    # take first frame as background
    ret, frame = cap.read()  # returns two values!
    background = frame

    # WHILE THERE ARE NEW FRAMES
    while cap.isOpened():
        ret, frame = cap.read()  # returns two values!

        # IF LAST FRAME REACHED STOP HERE
        if (ret == False):
            break

        foundBlobs = processImage(background, frame)

        if (len(foundBlobs) > 0):
            trackedTouches = tracker.track(foundBlobs)
            
            # Puttext
            for i in trackedTouches:
                xpos = i.positionx
                ypos = i.positiony
                cv2.putText(frame, "ID: " + str(i.id), (xpos, ypos), cv2.FONT_HERSHEY_SIMPLEX, 0.3, (0,255,0), 1, cv2.LINE_AA)
                ypos+=10
                cv2.putText(frame, "X: " + str(i.positionx), (xpos, ypos), cv2.FONT_HERSHEY_SIMPLEX, 0.3, (0,255,0), 1, cv2.LINE_AA)
                ypos+=10
                cv2.putText(frame, "Y: " + str(i.positiony), (xpos, ypos), cv2.FONT_HERSHEY_SIMPLEX, 0.3, (0,255,0), 1, cv2.LINE_AA)

            # TUIO SERVER - update the touches of the server with the touches from the tracker and send the bundle to the default TUIO client
            MyServer:MyTuioServer = MyTuioServer()
            MyServer.updateTouches(trackedTouches, cap.get(cv2.CAP_PROP_FRAME_WIDTH), cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

        cv2.imshow("INPUT", frame)

        # CUSTOM CLOSE ON ESC
        match cv2.waitKey(0):
            case 27:
                raise SystemExit
            case 0:
                continue

