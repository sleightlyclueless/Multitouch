import pygame
from pygame.locals import *
import pygame.color

from pythontuio import TuioClient, Cursor, TuioListener
from threading import Thread

from dollarpy import Template, Point, Recognizer

class MyListener(TuioListener):
    def __init__(self):
        self.cursor_paths = {}
        self.templates = [
            Template("Circle", [
                Point(127, 141), Point(124, 140), Point(120, 139), Point(118, 139),
                Point(116, 139), Point(111, 140), Point(109, 141), Point(104, 144),
                Point(100, 147), Point(96, 152), Point(93, 157), Point(90, 163),
                Point(87, 169), Point(85, 175), Point(83, 181), Point(82, 190),
                Point(82, 195), Point(83, 200), Point(84, 205), Point(88, 213),
                Point(91, 216), Point(96, 219), Point(103, 222), Point(108, 224),
                Point(111, 224), Point(120, 224), Point(133, 223), Point(142, 222),
                Point(152, 218), Point(160, 214), Point(167, 210), Point(173, 204),
                Point(178, 198), Point(179, 196), Point(182, 188), Point(182, 177),
                Point(178, 167), Point(170, 150), Point(163, 138), Point(152, 130),
                Point(143, 129), Point(140, 131), Point(129, 136), Point(126, 139)
            ]),
            Template("Tick", [
                Point(91, 185), Point(93, 185), Point(95, 185), Point(97, 185),
                Point(100, 188), Point(102, 189), Point(104, 190), Point(106, 193),
                Point(108, 195), Point(110, 198), Point(112, 201), Point(114, 204),
                Point(115, 207), Point(117, 210), Point(118, 212), Point(120, 214),
                Point(121, 217), Point(122, 219), Point(123, 222), Point(124, 224),
                Point(126, 226), Point(127, 229), Point(129, 231), Point(130, 233),
                Point(129, 231), Point(129, 228), Point(129, 226), Point(129, 224),
                Point(129, 221), Point(129, 218), Point(129, 212), Point(129, 208),
                Point(130, 198), Point(132, 189), Point(134, 182), Point(137, 173),
                Point(143, 164), Point(147, 157), Point(151, 151), Point(155, 144),
                Point(161, 137), Point(165, 131), Point(171, 122), Point(174, 118),
                Point(176, 114), Point(177, 112), Point(177, 114), Point(175, 116),
                Point(173, 118)
            ])
        ]
        self.recognizer = Recognizer(templates=self.templates)

    def add_tuio_cursor(self, cursor: Cursor) -> None:
        #print("Added {}".format(cursor.session_id))
        self.cursor_paths[cursor.session_id] = []  # Initialize an empty path for the cursor

    def update_tuio_cursor(self, cursor: Cursor) -> None:
        self.cursor_paths[cursor.session_id].append(cursor.position)  # Append the cursor position to its path
        self.recognize_gesture(cursor)  # Recognize gesture for the cursor

    def recognize_gesture(self, cursor: Cursor) -> None:
        path = self.cursor_paths[cursor.session_id]  # Get the path for the cursor
        print("Recoqnize gesture", path)
        if len(path) > 1:
            points = []
            for p in path:
                if len(p) >= 2 and all(isinstance(coord, (int, float)) and coord >= 0 for coord in p[:2]):
                    x = int(p[0] * 100)
                    y = int(p[1] * 100)
                    point = Point(x, y)
                    points.append(point)
            
            if points:
                gesture = self.recognizer.recognize(points)  # Pass the points individually
                print("Recognized gesture", gesture)

client = TuioClient(("localhost", 3333))
listener = MyListener()
client.add_listener(listener)

t = Thread(target=client.start)
t.start()

pygame.init()
WINDOW_SIZE = (800, 600)
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("TUIO Client")

def draw_number(number: int, x: int, y: int):
    font = pygame.font.Font(None, 25)  # Choose the desired font and size
    text_surface = font.render(str(number), True, (255, 255, 255))  # Render the text
    text_rect = text_surface.get_rect()
    text_rect.center = (x, y)  # Set the position of the text
    screen.blit(text_surface, text_rect)  # Draw the text onto the screen

def draw_cursors(cursors: list):
    screen.fill((0, 0, 0, 255))
    for curs in cursors:
        x, y = curs.position[0] * WINDOW_SIZE[0], curs.position[1] * WINDOW_SIZE[1]
        pygame.draw.circle(screen, (255, 0, 255, 255), (int(x), int(y)), 10)
        draw_number(curs.session_id, x, y)

        path = listener.cursor_paths[curs.session_id]  # Get the path for the cursor
        if len(path) > 1:
            scaled_path = [(p[0] * WINDOW_SIZE[0], p[1] * WINDOW_SIZE[1]) for p in path]
            pygame.draw.lines(screen, (255, 255, 255), False, scaled_path, 2)

def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

        mycurs = client.cursors
        draw_cursors(mycurs)

        pygame.display.flip()
        pygame.event.pump()  # Allow Pygame to handle events and update the TuioClient

    pygame.quit()

if __name__ == '__main__':
    main()