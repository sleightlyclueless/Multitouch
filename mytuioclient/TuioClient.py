import pygame
from pygame.locals import *
from pythontuio import TuioClient, Cursor, TuioListener
from threading import Thread
from math import hypot
from GeometricRecognizer import GeometricRecognizer  # Custom recognizer
from TuioGestures import Point2D

import GameMovingBlock
import random
import os

# Shapes from http://depts.washington.edu/acelab/proj/dollar/index.html
class MyListener(TuioListener):
    def __init__(self):
        self.cursor_paths = {}
        self.recognizer = GeometricRecognizer()
        self.recognizer.load_templates()
        # GAME
        self.blockList = list()
        self.score = 0
        self.game_over = False
        self.spawncooldown = 60
        self.spawntime = 60

        # Zoom
        self.last_zoom_distance = 0
        self.zoom_factor = 1.0

    def add_tuio_cursor(self, cursor: Cursor) -> None:
        self.cursor_paths[cursor.session_id] = []  # Initialize an empty path for the cursor

    def update_tuio_cursor(self, cursor: Cursor) -> None:
        cursor_path = self.cursor_paths.get(cursor.session_id)  # Get the path for the cursor
        if cursor_path is not None:
            last_position = cursor_path[-1] if cursor_path else None
            if cursor.position != last_position:
                cursor_path.append(Point2D(cursor.position[0], cursor.position[1]))  # Append the cursor position to its path

            # Zoom in an out on the game over image
            if self.game_over:
                screen.fill((0, 0, 0, 255))
                next_cursor_path = self.cursor_paths.get(cursor.session_id + 1)
                if cursor_path is not None and next_cursor_path is not None and len(next_cursor_path) > 0:
                    current_distance = hypot(cursor_path[0].x - next_cursor_path[-1].x, cursor_path[0].y - next_cursor_path[-1].y)
                    
                    if self.last_zoom_distance != 0:
                        if current_distance < self.last_zoom_distance:
                            self.zoom_factor *= 1.1  # Increase the zoom factor for zooming in
                        else:
                            self.zoom_factor *= 0.9  # Decrease the zoom factor for zooming out

                    self.last_zoom_distance = current_distance

    def remove_tuio_cursor(self, cursor: Cursor) -> None:
        if cursor.session_id in self.cursor_paths:
            path = self.cursor_paths[cursor.session_id]  # Get the path for the cursor

            if len(path) > 1:
                result = self.recognizer.recognize(path)  # Recognize gesture for the cursorpath
                print("Recognized gesture: " + result.Name + " with a score of " + str(result.Score))

            if not self.game_over:
                newlist = []  # check blocks and gesture recognition for next game frame
                for block in self.blockList:
                    if block.type.value != result.Name:
                        newlist.append(block)
                    else:
                        self.score += 100
                self.blockList = newlist
            else:
                self.cursor_paths = {}  # Reset the cursor paths if one is removed to avoid zoom gesture clashes


# TUIO Client
client = TuioClient(("localhost", 3333))
t = Thread(target=client.start)
listener = MyListener()
client.add_listener(listener)
t.start()

# PYGAME setup
pygame.init()
WINDOW_SIZE = (800, 600)
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("TUIO Client")
clock = pygame.time.Clock()
gamerunning = True

game_over_image = game_over_image = pygame.image.load(os.getcwd() + os.sep+"\mytuioclient\sprites"+os.sep+"game_over.png").convert_alpha()
game_over_image_rect = game_over_image.get_rect(center=(WINDOW_SIZE[0] / 2, WINDOW_SIZE[1] / 2))
zoomed_image = game_over_image.copy()
zoomed_image_rect = zoomed_image.get_rect(center=(WINDOW_SIZE[0] / 2, WINDOW_SIZE[1] / 2))


# Pygame helper functions
def draw_number(number, x, y):
    font = pygame.font.Font(None, 36)  # Choose the desired font and size
    text_surface = font.render(str(number), True, (255, 255, 255))  # Render the text
    text_rect = text_surface.get_rect()
    text_rect.center = (x, y)  # Set the position of the text
    screen.blit(text_surface, text_rect)  # Draw the text onto the screen


def draw_cursors(cursors: list):
    for curs in cursors:
        x, y = curs.position[0] * WINDOW_SIZE[0], curs.position[1] * WINDOW_SIZE[1]
        pygame.draw.circle(screen, (255, 0, 255, 255), (int(x), int(y)), 10)
        draw_number(curs.session_id, x, y)
        
        if curs.session_id in listener.cursor_paths:
            path = listener.cursor_paths[curs.session_id]  # Get the path for the cursor
            if len(path) > 1:
                scaled_path = [(p.x * WINDOW_SIZE[0], p.y * WINDOW_SIZE[1]) for p in path]
                pygame.draw.lines(screen, (255, 255, 255), False, scaled_path, 2)


def game():
    # draw the screen for the new frame
    screen.fill((0, 0, 0, 255))

    # spawn blocks
    listener.spawntime -= 1
    if listener.spawntime <= 0:
        rands = random.randint(1, 4)
        shape = GameMovingBlock.ShapeType.CHECKMARK
        if rands == 1:
            shape = GameMovingBlock.ShapeType.CHECKMARK
        elif rands == 2:
            shape = GameMovingBlock.ShapeType.CIRCLE
        elif rands == 3:
            shape = GameMovingBlock.ShapeType.DELETE
        elif rands == 4:
            shape = GameMovingBlock.ShapeType.TRIANGLE

        randx = random.randint(0, WINDOW_SIZE[0] - 50)

        listener.blockList.append(GameMovingBlock.MovingBlock(randx, 0, 50, 50, (255, 0, 0, 255), 1, shape, screen))
        listener.spawntime = listener.spawncooldown


    # update game objects
    for block in listener.blockList:
        block.update()

    # draw the game objects
    for block in listener.blockList:
        block.draw()
        if block.rect.y > WINDOW_SIZE[1]:
            listener.game_over = True
            return

    # draw the score
    draw_number("Score: " + str(listener.score), WINDOW_SIZE[0] / 2, 50)
    listener.game_over = False


def main():
    dorun = True

    while dorun:
        # custom exit handling on esc
        for event in pygame.event.get():
            if event.type == QUIT:
                dorun = False
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    dorun = False


        # game
        if not listener.game_over:
            game()        
        # game over image for zooming
        else:
            zoomed_image = pygame.transform.scale(game_over_image, (int(game_over_image_rect.width * listener.zoom_factor), int(game_over_image_rect.height * listener.zoom_factor)))
            zoomed_image_rect = zoomed_image.get_rect(center=(WINDOW_SIZE[0] / 2, WINDOW_SIZE[1] / 2))
            screen.blit(zoomed_image, zoomed_image_rect)


        # draw the cursors
        mycurs = client.cursors
        draw_cursors(mycurs)

        pygame.display.flip()
        pygame.event.pump()

        clock.tick(60)
    pygame.quit()


if __name__ == '__main__':
    main()