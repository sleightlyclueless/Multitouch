import pygame
from pygame.locals import *
import pygame.color

from pythontuio import TuioClient, Cursor, TuioListener
from threading import Thread
from TuioGestures import TuioGestures

from dollarpy import Point

class MyListener(TuioListener):
    def __init__(self):
        self.cursor_paths = {}
        self.gestures = TuioGestures()

    def add_tuio_cursor(self, cursor: Cursor) -> None:
        self.cursor_paths[cursor.session_id] = []  # Initialize an empty path for the cursor

    def update_tuio_cursor(self, cursor: Cursor) -> None:
        self.cursor_paths[cursor.session_id].append(cursor.position)  # Append the cursor position to its path
        self.recognize_gesture(cursor)  # Recognize gesture for the cursor

    def recognize_gesture(self, cursor: Cursor) -> None:
        path = self.cursor_paths[cursor.session_id]  # Get the path for the cursor
        if len(path) > 1:
            points = [Point(p[0], p[1]) for p in path if len(p) >= 2 and all(isinstance(coord, (int, float)) and coord >= 0 for coord in p[:2])]
            if points:
                gesture = self.gestures.recognize_gesture(points)  # Pass the points to TuioGestures
                if gesture and gesture[0] != None and gesture[0] != "":
                    print("Recognized gesture", gesture)


def draw_number(screen, number: int, x: int, y: int):
    font = pygame.font.Font(None, 25)  # Choose the desired font and size
    text_surface = font.render(str(number), True, (255, 255, 255))  # Render the text
    text_rect = text_surface.get_rect()
    text_rect.center = (x, y)  # Set the position of the text
    screen.blit(text_surface, text_rect)  # Draw the text onto the screen

def draw_cursors(screen, cursors: list, window_size):
    screen.fill((0, 0, 0, 255))
    for curs in cursors:
        x, y = curs.position[0] * window_size[0], curs.position[1] * window_size[1]
        pygame.draw.circle(screen, (255, 0, 255, 255), (int(x), int(y)), 10)
        draw_number(screen, curs.session_id, x, y)

        path = listener.cursor_paths[curs.session_id]  # Get the path for the cursor
        if len(path) > 1:
            scaled_path = [(p[0] * window_size[0], p[1] * window_size[1]) for p in path]
            pygame.draw.lines(screen, (255, 255, 255), False, scaled_path, 2)


client = TuioClient(("localhost", 3333))
listener = MyListener()
client.add_listener(listener)

t = Thread(target=client.start)
t.start()

pygame.init()
WINDOW_SIZE = (800, 600)
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("TUIO Client")

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
        draw_cursors(screen, mycurs, WINDOW_SIZE)

        pygame.display.flip()
        pygame.event.pump()  # Allow Pygame to handle events and update the TuioClient

    pygame.quit()

if __name__ == '__main__':
    main()