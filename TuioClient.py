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
            Template("Circle", [Point(0, 1), Point(0, 0.5), Point(0.5, 0), Point(1, 0.5), Point(1, 1), Point(0.5, 1)]),
            Template("Tick", [Point(0, 0), Point(0.4, 0.4), Point(1, 0)])
        ]
        self.recognizer = Recognizer(templates=self.templates)

    def add_tuio_cursor(self, cursor: Cursor):
        print("Added {}".format(cursor.session_id))
        self.cursor_paths[cursor.session_id] = []  # Initialize an empty path for the cursor

    def update_tuio_cursor(self, cursor: Cursor):
        self.cursor_paths[cursor.session_id].append(cursor.position)  # Append the cursor position to its path
        self.recognize_gesture(cursor)  # Recognize gesture for the cursor

    def recognize_gesture(self, cursor: Cursor):
        print("Recognizing gesture for cursor {} with path {}".format(cursor.session_id, self.cursor_paths[cursor.session_id]))


client = TuioClient(("localhost", 3333))
listener = MyListener()
client.add_listener(listener)

t = Thread(target=client.start)
t.start()

pygame.init()
WINDOW_SIZE = (800, 600)
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("TUIO Client")


def draw_number(number, x, y):
    font = pygame.font.Font(None, 25)  # Choose the desired font and size
    text_surface = font.render(str(number), True, (255, 255, 255))  # Render the text
    text_rect = text_surface.get_rect()
    text_rect.center = (x, y)  # Set the position of the text
    screen.blit(text_surface, text_rect)  # Draw the text onto the screen


def draw_cursors(cursors: list):
    screen.fill((0, 0, 0, 255))
    for curs in cursors:
        x, y = curs.position[0] * WINDOW_SIZE[0], curs.position[1] * WINDOW_SIZE[1]
        print("Drawing cursor {} at {}, {}".format(curs.session_id, x, y))
        pygame.draw.circle(screen, (255, 0, 255, 255), (int(x), int(y)), 10)
        draw_number(curs.session_id, x, y)

        path = listener.cursor_paths[curs.session_id]  # Get the path for the cursor
        print("Drawing path for cursor {} with path {}".format(curs.session_id, path))
        if len(path) > 1:
            pygame.draw.lines(screen, (255, 255, 255), False,
                              [(p[0] * WINDOW_SIZE[0], p[1] * WINDOW_SIZE[1]) for p in path], 2)


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

    pygame.quit()


if __name__ == '__main__':
    main()