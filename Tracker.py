# Tracker functionality to track cv blobs and interpret them as touches
from Blob import Blob
from Touch import Touch


class Tracker:
    def __init__(self, maxDistance: int):
        self.idcounter: int = 0
        self.touches: list = []
        self.maxDistance: int = maxDistance

    def track(self, _blobs: list):
        # for each touch check the closest blob as neighbour
        index: int = 0
        for currTouch in self.touches:
            self.find_nearest_neighbour(currTouch, index, _blobs)
            index += 1

        # for each blob that is left, create a new touch
        for i in _blobs:
            self.touches.append(Touch(self.idcounter, i.positionx, i.positiony))
            self.idcounter += 1

        return self.touches

    # compare blobs of current frame with touches of last frame and update touches for their nearest neighbour
    # 1 - if a blob is close to a touch, then the touch gets updated for next iteration and blob removed
    # 2 - if a blob is not close to a touch, then the touch gets removed but blob stays
    # Result: All Touches that are continued are updated and Blobs that were too far stay and get interpreted as new Touches above
    def find_nearest_neighbour(self, currTouch: Touch, index: int, _blobs: list):
        closestBlob: Blob = None
        closestDistance: int = None

        # search all blobs for the nearest neighbour
        for currBlob in _blobs:
            # calculate the distance in px (with pos values)
            dis: int = int(
                (
                    (currTouch.positionx - currBlob.positionx) ** 2
                    + (currTouch.positiony - currBlob.positiony) ** 2
                )
                ** 0.5
            )

            # if the smallest distance found is smaller than the max distance, then its a neighbour and that touch gets updated with the new position
            if dis < self.maxDistance:
                # if there is already a closest blob, check if the new one is closer
                if closestBlob != None:
                    if dis < closestDistance:
                        closestBlob = currBlob
                        closestDistance = dis
                else:
                    closestBlob = currBlob
                    closestDistance = dis

        # if there is no closest blob, then the touch is removed
        if closestBlob == None:
            self.touches.remove(currTouch)
        # if there is a closest blob, then the touch gets updated with the new position
        else:
            self.touches[index].positionx = closestBlob.positionx
            self.touches[index].positiony = closestBlob.positiony
            _blobs.remove(closestBlob)
