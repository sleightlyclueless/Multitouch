from Blob import Blob
from Touch import Touch


class Tracker:
    def __init__(self, maxdistance:int):
        self.idcounter:int = 0
        self.touches:list = []
        self.maxdistance:int = maxdistance

    def track(self, _blobs:list):
        # for each touch check the closest blob as neighbour
        index:int = 0
        for currTouch in self.touches:
            self.findNearestNeighbour(currTouch, index, _blobs)
            index+=1

        # just add remaining touches if there are new ones
        for i in _blobs:
            self.touches.append(Touch(self.idcounter, i.positionx, i.positiony))
            self.idcounter += 1

        return self.touches


    def findNearestNeighbour(self, currTouch:Touch, index:int, _blobs:list):
        closestBlob:Blob = None
        closestDistance:int = None

        currTouchPos:Touch = [currTouch.positionx, currTouch.positiony]

        #search all blobs for the nearest neighbour
        for currBlob in _blobs:
            currBlobPos:Touch = [currBlob.positionx, currBlob.positiony]
            
            #calculate the distance (with pos values)
            dis:int = int(((currTouchPos[0] - currBlobPos[0]) ** 2 + (currTouchPos[1] - currBlobPos[1]) ** 2) ** 0.5)
            if (dis < self.maxdistance):
                if (closestBlob != None):
                    if (dis < closestDistance):
                        closestBlob = currBlob
                        closestDistance = dis
                else:
                    closestBlob = currBlob
                    closestDistance = dis

        # remove prev touch if no closest found and hence its gone
        if (closestBlob == None):
            self.touches.remove(currTouch)
        else:
            self.touches[index].positionx = closestBlob.positionx
            self.touches[index].positiony = closestBlob.positiony
            _blobs.remove(closestBlob)
