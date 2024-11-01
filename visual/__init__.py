"""
visual

this module contains methods to display the map and manage all the actions that ocurs in it
"""

import pygame as pg
from pygame.locals import *

global WIDTH
global HEIGHT
global WLINES
global HLINES

WIDTH = 1000
HEIGHT = 600
BGCOLOR = (150,150,150)
LCOLOR = (0,0,0)
CELLCOLOR = (0,0,255)
WLINES = 100
HLINES = 100

def draw_table(screen,size,grid):
    w,h = size
    w_g,h_g = grid
    h_w = h / w_g
    v_w = w / h_g
    
    # for i in range(w_g):
    #     pg.draw.line(screen,LCOLOR,(0,i*h_w),(WIDTH,i*h_w))
    #     pass
    # for i in range(h_g):
    #     pg.draw.line(screen,LCOLOR,(i*v_w,0),(i*v_w,HEIGHT))
    #     pass
    
    return v_w - 2,h_w - 2

def draw_cell(screen,pos,cell_size):
    w,h = cell_size
    x,y = pos
    pg.draw.rect(screen,CELLCOLOR,(x + 1,y + 1,w,h))
    pass

def geometry(size):
    global WIDTH
    global HEIGHT
    
    WIDTH = size[0]
    HEIGHT = size[1]
    pass

def grid(x,y):
    global WLINES
    global HLINES
    
    WLINES = x
    HLINES = y
    pass

def init(xlines,ylines):
    grid(xlines,ylines)
    pass

def run(generator):
    global WIDTH
    global HEIGHT
    global WLINES
    global HLINES
    
    pg.init()
    main_clock = pg.time.Clock()
    SCREEN = pg.display.set_mode((WIDTH,HEIGHT))
    width,height = draw_table(SCREEN,(WIDTH,HEIGHT),(WLINES,HLINES))
        
    while generator.next:
        pass
        
    SCREEN.fill(BGCOLOR)
        
    for i in range(generator.map.shape[0]):
        for j in range(generator.map.shape[1]):
            if generator.map[i,j] == -1:
                draw_cell(SCREEN,(i*(width + 2),j*(height + 2)),(width,height))
                pass
            pass
        pass
    
    pg.display.update()
    main_clock.tick(60)
        
    
    pass