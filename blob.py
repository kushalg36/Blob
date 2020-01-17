import pygame
import random
from blobClass import Blob
import numpy as np

WIDTH = 800
HEIGHT = 600
WHITE = (255,255,255)
BLUE = (0,0,255)
RED = (255,0,0)
GREEN = (0,255,0)
STARTING_RED_BLOBS=3
STARTING_BLUE_BLOBS=10
STARTING_GREEN_BLOBS=3

game_display = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Blob World')
clock = pygame.time.Clock()

class BlueBlob(Blob):
    def __init__(self,x_bound,y_bound):
        super().__init__(BLUE,x_bound,y_bound)

    def __add__(self, other_blob):
        if other_blob.color == (255,0,0):
            self.size -= other_blob.size
            other_blob.size = 0
        elif other_blob.color == (0,255,0):
            self.size += other_blob.size
            other_blob.size = 0
        elif other_blob.color == (0,0,255):
            pass

class RedBlob(Blob):
    def __init__(self,x_bound,y_bound):
        super().__init__(RED,x_bound,y_bound)

class GreenBlob(Blob):
    def __init__(self,x_bound,y_bound):
        super().__init__(GREEN,x_bound,y_bound)

def isTouching(b1,b2):
    return (np.linalg.norm(abs(np.array([b1.x,b1.y])-np.array([b2.x,b2.y]))) < (b1.size + b2.size))

def handleCollision(blobs):
    blues, reds, greens = blobs
    for blue_id, blue_blob in blues.copy().items():
        for other_blobs in blues, reds, greens:
            for other_blob_id,other_blob in other_blobs.copy().items():
                if blue_blob == other_blob:
                    pass
                else:
                    if isTouching(blue_blob, other_blob):
                        blue_blob + other_blob
                    if other_blob.size <= 0:
                        # del other_blobs[other_blob_id]
                        other_blobs.pop(other_blob_id,None)
                    if blue_blob.size <= 0:
                        # del blues[blue_id]
                        blues.pop(other_blob_id,None)
    return blues, reds, greens

def draw_enviroment(blobs):
    blues, reds, greens = handleCollision(blobs)
    game_display.fill(WHITE)
    for blob_dict in blobs:
        for blob_id in blob_dict:
            blob = blob_dict[blob_id]
            pygame.draw.circle(game_display,blob.color, [blob.x,blob.y],blob.size)
            blob.move()
            # print(blob.x,blob.y)
    pygame.display.update()
    return blues, reds, greens

def main():
    blue_blob = dict(enumerate([BlueBlob(WIDTH,HEIGHT) for i in range(STARTING_BLUE_BLOBS)]))
    red_blob = dict(enumerate([RedBlob(WIDTH,HEIGHT) for i in range(STARTING_RED_BLOBS)]))
    green_blob = dict(enumerate([GreenBlob(WIDTH,HEIGHT) for i in range(STARTING_GREEN_BLOBS)]))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        blues, reds, greens = draw_enviroment([blue_blob,red_blob,green_blob])
        clock.tick(60)
        
if __name__ == '__main__':
    main()