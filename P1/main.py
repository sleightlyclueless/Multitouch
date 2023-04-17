import cv2;

cap = cv2.VideoCapture("../mt_camera_raw.AVI")
_BlurHighPass = 15 #first opening & closing
_BlurSmoothing = 3 #second opening & closing
# _BlurSmoothing = 6 #second opening & closing
_Threshold = 9.5


if cap:
    currFrame = 0
    
    while cap.isOpened():
        ret, frame = cap.read() #returns two values!

        if currFrame == 0:
            background = frame

        if (ret == False):
            break
        

        if currFrame > 0:
            diffImage = cv2.absdiff(background, frame)
            blurImage = cv2.blur(diffImage, (_BlurHighPass,_BlurHighPass))

            diffImage2 = cv2.absdiff(blurImage, diffImage)
            blurImage2 = cv2.blur(diffImage2, (_BlurSmoothing,_BlurSmoothing))

            grayImage = cv2.cvtColor(blurImage2, cv2.COLOR_BGR2GRAY)
            ret, thresholdImage = cv2.threshold(grayImage, _Threshold, 255, cv2.THRESH_BINARY) #returns two values!


            contours, hierarchy = cv2.findContours(thresholdImage, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)
            if hierarchy is not None:
                for idx in range(len(hierarchy[0])):
                    if cv2.contourArea(contours[idx]) > 10 and len(contours[idx]) > 4: # clots with 10px +
                        cv2.ellipse(frame, cv2.fitEllipse(contours[idx]), (0,0,255), 1, cv2.LINE_AA)
                        cv2.drawContours(frame, contours, idx, (255,0,0), 1, cv2.LINE_AA, hierarchy=hierarchy)


            cv2.imshow("0INPUT", frame)
            cv2.imshow("1diffImage", diffImage)
            cv2.imshow("2blurImage", blurImage)
            cv2.imshow("3diffImage2", diffImage2)
            cv2.imshow("4blurImage2", blurImage2)
            cv2.imshow("5thresholdImage", thresholdImage)


            # Custom close on esc
            match cv2.waitKey(0):
                case 27:
                    raise SystemExit
                case 0:
                    continue

        currFrame =+ 1