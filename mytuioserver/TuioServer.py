# pip install python-tuio
from Touch import Touch
from pythontuio import TuioServer, Cursor


class MyTuioServer:
    def __init__(self) -> None:
        self.server = (
            TuioServer()
        )  # create a new server on localhost, port 3333 as per default from TUIO python library on init
        self.trackedIds: list() = list()  # hold a list of all tracked ids

    # update_touches: update the touches of the server with the touches from the tracker and send the bundle to the default TUIO client
    def update_touches(self, touchesList: list(), screenw: int, screenh: int):
        touches: Touch

        # check all touches for the current frame (already interpreted as Touch by Tracker.py)
        for touches in touchesList:
            if touches.id not in self.trackedIds:  # not tracked yet: add to list
                curs = Cursor(touches.id)
                curs.position = (
                    touches.positionx / screenw,
                    touches.positiony / screenh,
                )  # normalize between 0 and 1
                self.server.cursors.append(curs)
                self.trackedIds.append(touches.id)

            else:  # already tracked: update position
                curs: Cursor
                for curs in self.server.cursors:
                    if curs.session_id == touches.id:
                        curs.position = (
                            touches.positionx / screenw,
                            touches.positiony / screenh,
                        )

        # send bundle to tuio client (done every frame and removing all cursors that are not tracked anymore by TUIO client)
        self.server.send_bundle()
