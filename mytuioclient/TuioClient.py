import pygame
from pygame.locals import *
from pythontuio import TuioClient, Cursor, TuioListener
from threading import Thread
from math import hypot
from GeometricRecognizer import GeometricRecognizer  # Custom recognizer
from TuioGestures import Point2D

import GameMovingBlock
import GameOverRect
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
        self.score:int = 0
        self.game_over:bool = False
        self.spawncooldown:int = 60
        self.spawntime:int = 60
        self.gameOverRect = None
        self.clocktime:int = 60
        self.handlegameover:bool = False

        # Zoom
        self.last_zoom_distance:float = 0
        self.zoom_factor:float = 1.0

    def add_tuio_cursor(self, cursor: Cursor) -> None:
        self.cursor_paths[cursor.session_id] = []  # Initialize an empty path for the cursor

    def update_tuio_cursor(self, cursor: Cursor) -> None:
        cursor_path:list = self.cursor_paths.get(cursor.session_id)  # Get the path for the cursor
        if cursor_path is not None:
            last_position = cursor_path[-1] if cursor_path else None
            if cursor.position != last_position:
                cursor_path.append(Point2D(cursor.position[0], cursor.position[1]))  # Append the cursor position to its path

            # Zoom in an out on the game over image
            if self.game_over:
                self.spawncooldown = 60
                self.clocktime = 60
                next_cursor_path:list = self.cursor_paths.get(cursor.session_id + 1)
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

            result = None
            if len(path) > 1:
                result = self.recognizer.recognize(path)  # Recognize gesture for the cursorpath
                if (result.Score > 0.75 and result.Name != "Unknown"):
                    print("Recognized gesture: " + result.Name + " with a score of " + str(result.Score))
                else:
                    result = None
                    

            if not self.game_over and result:
                newlist = []  # check blocks and gesture recognition for next game frame
                for block in self.blockList:
                    if block.type.value != result.Name:
                        newlist.append(block)
                    else:
                        self.score += 100
                        self.spawncooldown *= 0.99
                        self.clocktime += 1
                self.blockList = newlist
            else:
                if (self.handlegameover):
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

        # draw the screen for the new frame
        screen.fill((0, 0, 0, 255))

        # game
        if not listener.game_over:
            game()        
        # game over image for zooming
        else:
            if listener.handlegameover:
                listener.gameOverRect = GameOverRect.GameOverRect(0,0,WINDOW_SIZE[0], WINDOW_SIZE[1],screen)
                listener.gameOverRect.draw(listener.zoom_factor)

                font = pygame.font.Font(None, 36)  # Choose the desired font and size
                text_surface = font.render("Game Over - Zoom To Restart", True, (255, 255, 255))  # Render the text
                text_rect = text_surface.get_rect()
                text_rect.center = (WINDOW_SIZE[0]/2, WINDOW_SIZE[1]/2)  # Set the position of the text
                screen.blit(text_surface, text_rect)  # Draw the text onto the screen

                if(listener.gameOverRect.drawn_rect_width > WINDOW_SIZE[0]): # zoomed and start new game
                    print("New game")
                    listener.score = 0
                    listener.game_over = False
                    listener.spawncooldown = 60
                    listener.spawntime = 60
                    listener.last_zoom_distance = 0
                    listener.zoom_factor = 1.0
                    listener.gameOverRect = None
                    listener.blockList = []

            # draw the score
            draw_number("Score: " + str(listener.score), WINDOW_SIZE[0] / 2, 50)

        # draw the cursors
        mycurs = client.cursors
        draw_cursors(mycurs)

        pygame.display.flip()
        pygame.event.pump()

        clock.tick(listener.clocktime)
    pygame.quit()


if __name__ == '__main__':
    main()