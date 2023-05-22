# pip install python-osc
from pythonosc import udp_client

class TuioServer:
    def __init__(self, host='127.0.0.1', port=3333):
        self.host = host
        self.port = port
        self.client = udp_client.SimpleUDPClient(self.host, self.port)

    def sendBlob(self, blob):
        # Send TUIO "set" message for adding/updating a blob
        self.client.send_message("/tuio/2Dcur", "/tuio/2Dcur", ["set", blob.id, blob.positionx, blob.positiony])

    def removeBlob(self, blob):
        # Send TUIO "fseq" message for removing a blob
        self.client.send_message("/tuio/2Dcur", "/tuio/2Dcur", ["fseq", blob.id])