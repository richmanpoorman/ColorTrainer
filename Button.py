from UserInput import UserInput
from Interactable import Interactable

from pygame import Surface


class Button(Interactable):

    def __init__(self, position : tuple, size : tuple, callback, color : tuple = (0, 0, 0), isActive = True):
        '''
            Purpose    : 
            Parameters : 
            Return     :
        '''
        surface = Surface(size)
        surface.fill(color)
        self.setSurface(surface)
        super().__init__(position, size, surface = surface, isActive = isActive)
        self.callback = callback 
        

    def onLeftClick(self, mousePos : tuple):
        '''
            Purpose    : Calls the callback when left clicked
            Parameters : (tuple) mousePos := The mouse position
            Return     : None
        '''
        self.callback()
        