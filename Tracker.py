from Blob import Blob
from Touch import Touch


class Tracker:
    def __init__(self, touches, maxdistance):
        self.idcounter = 0
        self.touches = touches
        self.maxdistance = maxdistance

    def track(self, _blobs):
        # for each touch check the closest blob as neighbour
        index = 0
        for currTouch in self.touches:
            self.findNearestNeighbour(currTouch, index, _blobs)
            index+=1

        # just add remaining touches if there are new ones
        for i in _blobs:
            self.touches.append(Touch(self.idcounter, i.positionx, i.positiony))
            self.idcounter += 1

        return self.touches


    def findNearestNeighbour(self, currTouch, index, _blobs):
        closestBlob = None
        closestDistance = None

        currTouchPos = [currTouch.positionx, currTouch.positiony]

        #search all blobs for the nearest neighbour
        for currBlob in _blobs:
            currBlobPos = [currBlob.positionx, currBlob.positiony]
            
            #calculate the distance
            dis = int(((currTouchPos[0] - currBlobPos[0]) ** 2 + (currTouchPos[1] - currBlobPos[1]) ** 2) ** 0.5)
            if (closestBlob != None):
                if (dis < self.maxdistance and dis < closestDistance):
                    closestBlob = currBlob
                    closestDistance = dis
            else:
                if (dis < self.maxdistance):
                    closestBlob = currBlob
                    closestDistance = dis

        # remove prev touch if no closest found and hence its gone
        if (closestBlob == None):
            self.touches.remove(currTouch)
        else:
            self.touches[index].positionx = closestBlob.positionx
            self.touches[index].positiony = closestBlob.positiony
            _blobs.remove(closestBlob)
