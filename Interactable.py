from Displayable import Displayable
from UserInput import UserInput
from pygame import Surface

class Interactable(Displayable):

    def __init__(self, position : tuple, size : tuple, surface : Surface = None, isActive : bool = True):
        '''
            Purpose    : Creates an object which can be clicked on with the mouse
            Parameters : (tuple) position := Position on the screen
                         (tuple) size     := The size of the object
        '''
        super().__init__(position, size, surface, isActive) 
        self.__isDrag       = False
        self.leftClickID    = UserInput.onMouseDown(self.__whenPressed(self.onLeftClick, True), UserInput.LEFT_CLICK)
        self.leftReleaseID  = UserInput.onMouseUp(self.__whenPressed(self.onLeftRelease, False), UserInput.LEFT_CLICK)
        self.rightClickID   = UserInput.onMouseDown(self.__whenPressed(self.onRightClick, True), UserInput.RIGHT_CLICK)
        self.rightReleaseID = UserInput.onMouseUp(self.__whenPressed(self.onRightRelease, False), UserInput.RIGHT_CLICK)
        self.dragID         = UserInput.onMouseMove(self.__whenDrag())
    
    def __del__(self):
        self.removeListeners()

    def removeListeners(self):
        UserInput.removeMouseDown(UserInput.LEFT_CLICK, self.leftClickID)
        UserInput.removeMouseUp(UserInput.LEFT_CLICK, self.leftReleaseID)
        UserInput.removeMouseDown(UserInput.RIGHT_CLICK, self.rightClickID)
        UserInput.removeMouseUp(UserInput.RIGHT_CLICK, self.rightReleaseID)
        UserInput.removeMouseMove(self.dragID)

    def __whenPressed(self, callable, isClick):
        '''
            Purpose    : Wrapper for click/release to only be when on interaction
            Parameters : (function) callable := On click/release function
            Return     : (function) callback function for the listener
        '''
        def whenClickOrRelease(mousePos : tuple):
            if self.isActive() and self.isOnInteractable(mousePos):
                self.__isDrag = isClick
                callable(mousePos)
            else:
                self.__isDrag = False
                
        return whenClickOrRelease

    def __whenDrag(self):
        '''
            Purpose    : Wrapper for mouse movement
            Parameters : (function) callable := On click/release function
            Return     : (function) callback function for the listener
        '''
        def whenDrag(rel : tuple, mousePos : tuple):
            if not self.isActive():
                return 
            if self.__isDrag:
                if self.isOnInteractable(mousePos):
                        self.onDrag(rel, mousePos)
                else:
                    self.onLeftRelease(mousePos)
                    self.onRightRelease(mousePos)
                    self.__isDrag = False
        return whenDrag 
    

    def isOnInteractable(self, mousePos : tuple):
        '''
            Purpose    : Checks if the mouse position is in the interactable
            Parameters : (tuple) mousePos := The mouse position on the screen
            Return     : (bool) Whether or not it is on the interactable
        '''
        if not self.isActive:
            return False
        x, y = mousePos 
        x1, y1 = self.position 
        w, h = self.size 
        return x >= x1 and x <= x1 + w and y >= y1 and y <= y1 + h
    


    def onLeftClick(self, mousePos : tuple):
        pass

    def onLeftRelease(self, mousePos : tuple):
        pass
    
    def onRightClick(self, mousePos : tuple):
        pass 

    def onRightRelease(self, mousePos : tuple):
        pass 

    def onDrag(self, rel : tuple, mousePos : tuple):
        pass


