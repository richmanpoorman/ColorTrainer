from pygame import Surface 
class Displayable:
    def __init__(self, position : tuple, size : tuple, surface : Surface = None, isActive : bool = True):
        '''
            Purpose    : 
            Parameters : 
            Return     :
        '''
        self.position = position 
        self.size     = size  
        self.surface  = Surface(size) if not surface else surface 
        self.__isActive = isActive
    
    def getPosition(self):
        '''
            Purpose    : 
            Parameters : 
            Return     :
        '''
        return self.position
    
    def getSize(self):
        '''
            Purpose    : 
            Parameters : 
            Return     :
        '''
        return self.size
    
    def getSurface(self):
        '''
            Purpose    : 
            Parameters : 
            Return     :
        '''
        return self.surface if self.isActive else None
    
    def isActive(self):
        '''
            Purpose    : 
            Parameters : 
            Return     :
        '''
        return self.__isActive

    def setPosition(self, position : tuple):
        '''
            Purpose    : 
            Parameters : 
            Return     :
        '''
        self.position = position 
    
    def setSize(self, size : tuple):
        '''
            Purpose    : 
            Parameters : 
            Return     :
        '''
        self.size = size 
    
    def setSurface(self, surface : Surface):
        '''
            Purpose    : 
            Parameters : 
            Return     :
        '''
        self.surface = surface

    def activate(self):
        '''
            Purpose    : 
            Parameters : 
            Return     :
        '''
        self.__isActive = True 

    def deactivate(self):
        '''
            Purpose    : 
            Parameters : 
            Return     :
        '''
        self.__isActive = False