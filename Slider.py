from Interactable import Interactable
from pygame import Surface 
import pygame

class Slider(Interactable):
    
    def __init__(self, position : tuple, size : tuple, sliderBG : Surface = None, knob : Surface = None): 
        super().__init__(position, size)
        if not sliderBG:
            sliderBG = self.__defaultBG()
        if not knob:
            knob = self.__defaultKnob()
        self.blankBack = Surface(size, pygame.SRCALPHA)
        self.knobPos   = 0
        self.sliderBG  = pygame.transform.scale(sliderBG, size)
        w, h           = size 
        knobLength     = min(w, h)
        self.knobSize  = (knobLength, knobLength)
        self.knob      = pygame.transform.scale(knob, self.knobSize)
        
        self.isKnobDrag = False
        self.__updateSurface()


    def onKnobChange(self):
        pass

    def onLeftClick(self, mousePos : tuple):
        mouseX, _ = mousePos 
        x, _ = self.getPosition() 
        w, _ = self.getSize() 

        self.knobPos = (mouseX - x) / w
        self.isKnobDrag = True 
        self.onKnobChange()
    
    def onDrag(self, rel : tuple, mousePos : tuple):
        if not self.isKnobDrag:
            return 
        
        mouseX, _ = mousePos 
        x, _ = self.getPosition() 
        w, _ = self.getSize() 

        self.knobPos = (mouseX - x) / w
        self.__updateSurface()
        self.onKnobChange()

    def onLeftRelease(self, mousePos : tuple):
        self.isKnobDrag = False

    def isMouseOnKnob(self, mousePos : tuple):
        mouseX, _ = mousePos
        x, _ = self.getPosition()
        w, _ = self.getSize()
        knobW, _ = self.knobSize

        knobPos = w * self.knobPos 
        knobHalf = knobW // 2

        return x + knobPos - knobHalf <= mouseX and mouseX <= x + knobPos + knobHalf 
    
    def __updateSurface(self):
        w, h = self.getSize()
        knobW, _ = self.knobSize
        surface = Surface((w, h), pygame.SRCALPHA)
        surface.blit(self.sliderBG, (0, 0))
        surface.blit(self.knob, (self.knobPos * w - knobW // 2, 0))
        self.setSurface(surface)

    def updateBG(self, bg : Surface): 
        self.sliderBG  = pygame.transform.scale(bg, self.getSize())
        self.__updateSurface()

    def updateKnob(self, knob : Surface):
        self.knob = pygame.transform.scale(knob, self.knobSize)
        self.__updateSurface()

    def getKnobValue(self):
        return self.knobPos
    
    
    def onLeftRelease(self, mousePos: tuple):
        self.knobPos = False

    def __defaultBG(self):
        surface = Surface((1, 1))
        surface.fill((255, 0, 0))
        return surface
    
    def __defaultKnob(self):
        w, h = self.getSize() 
        size = min(w, h)
        surface = Surface((size, size))
        surface.fill((0, 0, 255))
        return surface