# pip install python-tuio
from Touch import Touch
from pythontuio import TuioServer, Cursor

class MyTuioServer:
    def __init__(self) -> None:
        self.server = TuioServer() # create a new server on localhost, port 3333 as per default from TUIO python library on init
        self.trackedIds = list() # hold a list of all tracked ids
    

    # updateTouches: update the touches of the server with the touches from the tracker and send the bundle to the default TUIO client
    def updateTouches(self, touchesList, screenw, screenh):
        for touches in touchesList:
            if touches.id not in self.trackedIds:
                curs = Cursor(touches.id)
                curs.position = (touches.positionx / screenw, touches.positiony / screenh)
                self.server.cursors.append(curs)
                self.trackedIds.append(touches.id)
            else:
                for curs in self.server.cursors:
                    if curs.session_id == touches.id:
                        curs.position = (touches.positionx / screenw, touches.positiony / screenh)
                        curs.path.append(curs.position)  # Append the cursor position to its path

        # send bundle to TUIO client (done every frame and removing all cursors that are not tracked anymore by TUIO client)
        self.server.send_bundle()