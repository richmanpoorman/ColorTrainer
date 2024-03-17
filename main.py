import pygame 
from Display import Display
from UserInput import UserInput

class Runner:
    def __init__(self):
        '''
            Purpose    : 
            Parameters : 
            Return     :
        '''
        pygame.init()
        self.isRunning = True 
        screen = Display()

        UserInput.onQuit(self.quit)

        while self.isRunning: 
            screen.update()
            UserInput.check()
        pygame.quit()
    
    def quit(self):
        '''
            Purpose    : 
            Parameters : 
            Return     :
        '''
        self.isRunning = False 

    
Runner()
