# Basic structure of a identified touch
class Touch:
    def __init__(self, id: int, positionx: int, positiony: int):
        self.id: int = id
        self.positionx: int = positionx
        self.positiony: int = positiony
