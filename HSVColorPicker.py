from pygame import Surface
from pygame import draw
import pygame
from math import ceil
from UserInput import UserInput 
from Interactable import Interactable

class HSVColorPicker(Interactable):
    DEFINITION = 128
    CIRCLE_RADIUS = 5
    CIRCLE_THICKNESS = 2

    def __init__(self, position : tuple, size : tuple, chroma : int = 0, sv : tuple = (0.0, 0.0)):
        '''
            Purpose    : 
            Parameters : 
            Return     :
        '''
        super().__init__(position, size)
        self.h        = chroma
        self.sv       = sv
        self.grid     = Surface(size)
        self.circle   = Surface((HSVColorPicker.CIRCLE_RADIUS * 2, HSVColorPicker.CIRCLE_RADIUS * 2), pygame.SRCALPHA)
        self.circle.fill((0, 0, 0, 0))
        self.updateChroma(chroma)
        self.isDrag   = False

    def onLeftClick(self, mousePos : tuple):
        '''
            Purpose    : 
            Parameters : 
            Return     :
        '''
        self.mousePositionCircle(mousePos)

    def onDrag(self, rel : tuple, mousePos : tuple):
        self.mousePositionCircle(mousePos)
    
    def mousePositionCircle(self, mousePos : tuple):
        x, y = mousePos 
        x1, y1 = self.getPosition() 
        w, h = self.getSize()
        x -= x1 
        y -= y1 

        sv = (x / w, y / h)
        self.updateCircle(sv)

    def getColor(self):
        '''
            Purpose    : 
            Parameters : 
            Return     :
        '''
        s, v = self.sv
        return HSVColorPicker.HSVToRGB((self.h, s, v))

    def updateChroma(self, newChroma : int):
        '''
            Purpose    : 
            Parameters : 
            Return     :
        '''
        self.h       = newChroma
        w, h         = self.getSize() 
        numBlocks    = HSVColorPicker.DEFINITION
        blockWidth   = w / numBlocks
        blockHeight  = h / numBlocks
        rBlockWidth  = ceil(blockWidth)
        rBlockHeight = ceil(blockHeight)

        for r in range(numBlocks):
            for c in range(numBlocks):
                color = HSVColorPicker.HSVToRGB((self.h, r / numBlocks, c / numBlocks))
                x, y = round(r * blockWidth), round(c * blockHeight)
                rect = (x, y, rBlockWidth, rBlockHeight)
                draw.rect(self.grid, color, rect)
        self.updateCircle(self.sv)
        

    def updateCircle(self, newSV : tuple):
        '''
            Purpose    : 
            Parameters : 
            Return     :
        '''
        self.sv = newSV 
        s, v    = newSV 
        color   = HSVColorPicker.HSVToRGB((self.h, s, v))
        circleR = HSVColorPicker.CIRCLE_RADIUS
        draw.circle(self.circle, color, (circleR, circleR), circleR)
        draw.circle(self.circle, (0, 0, 0), (circleR, circleR), circleR, HSVColorPicker.CIRCLE_THICKNESS)
        self.updateSurface()

    def updateSurface(self):
        '''
            Purpose    : 
            Parameters : 
            Return     :
        '''
        s, v = self.sv 
        w, h = self.getSize()
        s = round(s * w) - HSVColorPicker.CIRCLE_RADIUS 
        v = round(v * h) - HSVColorPicker.CIRCLE_RADIUS 
        surface = Surface(self.getSize())
        surface.blit(self.grid, (0, 0))
        surface.blit(self.circle, (s, v))
        self.setSurface(surface)

    def HSVToRGB(hsv : tuple):
        '''
            Purpose    : 
            Parameters : 
            Return     :
        '''
        h, s, v = hsv 
        c = v * s 
        x = c * (1 - abs((h / 60) % 2 - 1))
        m = v - c 
        rP, gP, bP = (c, x, 0) if 0   <= h and h < 60  else \
                     (x, c, 0) if 60  <= h and h < 120 else \
                     (0, c, x) if 120 <= h and h < 180 else \
                     (0, x, c) if 180 <= h and h < 240 else \
                     (x, 0, c) if 240 <= h and h < 300 else \
                     (c, 0, x) if 300 <= h and h < 360 else \
                     None
        r, g, b = ((rP + m) * 255, (gP + m) * 255, (bP + m) * 255)
        return (round(r), round(g), round(b))
    
    
        


