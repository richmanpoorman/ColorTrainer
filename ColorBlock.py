from pygame import Surface
from random import randint 

class ColorBlock: 

    def __init__(self, position : tuple, size : tuple, color : tuple = (0, 0, 0)):
        '''
            Purpose    : 
            Parameters : 
            Return     :
        '''
        self.size     = size
        self.color    = color 
        self.position = position
        self.block    = Surface(size)
        self.setColor(color)
        
    def setColor(self, color : tuple):
        '''
            Purpose    : 
            Parameters : 
            Return     :
        '''
        self.color = color 
        self.block.fill(color)

    def setRandomColor(self):
        '''
            Purpose    : 
            Parameters : 
            Return     :
        '''
        randColor = (randint(0, 255), randint(0, 255), randint(0, 255))
        self.setColor(randColor)
    
    def getSurface(self):
        '''
            Purpose    : 
            Parameters : 
            Return     :
        '''
        return self.block
    
    def getPosition(self):
        '''
            Purpose    : 
            Parameters : 
            Return     :
        '''
        return self.position
    