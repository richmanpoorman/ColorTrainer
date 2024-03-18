import pygame 
from ColorBlock import ColorBlock
from Button import Button
from HSVColorPicker import HSVColorPicker
from HSVSlider import HSVSlider
class Display:

    def __init__(self):
        '''
            Purpose    : 
            Parameters : 
            Return     :
        '''
        self.screen = pygame.display.set_mode((700, 700))

        self.goal      = ColorBlock((100, 100), (200, 200))
        self.randomize = Button((100, 325), (200, 50), self.goal.setRandomColor, (255, 255, 255))
        self.picker    = HSVColorPicker((300, 300), (300, 300), sv = (0.5, 0.5))
        self.picked    = ColorBlock((300, 100), (200, 200))
        self.slider    = HSVSlider((50, 500), (200, 25), self.picker)
        self.goal.setRandomColor()

    def __updateDisplay(self):
        '''
            Purpose    : 
            Parameters : 
            Return     :
        '''
        goalBlock = self.goal.getSurface()
        goalPos   = self.goal.getPosition()
        self.screen.blit(goalBlock, goalPos)

        buttonSurface = self.randomize.getSurface()
        buttonPos     = self.randomize.getPosition()
        self.screen.blit(buttonSurface, buttonPos)

        pickerSurface = self.picker.getSurface() 
        pickerPos     = self.picker.getPosition() 
        self.screen.blit(pickerSurface, pickerPos)

        self.picked.setColor(self.picker.getColor())
        pickedSurface = self.picked.getSurface() 
        pickedPos     = self.picked.getPosition() 
        self.screen.blit(pickedSurface, pickedPos)

        sliderSurface = self.slider.getSurface() 
        sliderPos     = self.slider.getPosition()
        self.screen.blit(sliderSurface, sliderPos)

    
    def update(self):
        '''
            Purpose    : 
            Parameters : 
            Return     :
        '''
        self.__updateDisplay() 
        pygame.display.update()
