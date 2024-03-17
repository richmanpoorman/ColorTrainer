import pygame

class UserInput:
    __listeners = dict() 
    __id        = 0

    LEFT_CLICK  = 1 
    MOUSE_WHEEL = 2
    RIGHT_CLICK = 3

    ''' CALLABLE FUNCTIONS '''
    @staticmethod
    def onQuit(callback):
        '''
            Purpose    : Calls the given callback function when quitting
            Parameters : (function) callback := The function to call on quit
            Return     : (int) An ID representing the listener (for removal)
        '''
        return UserInput.__addListener(pygame.QUIT, None, callback)
    
    @staticmethod
    def removeQuit(id):
        '''
            Purpose    : Remove the given ids from the quit call
            Parameters : (int) id := Id which are callbacks called on quit
            Return     : (None)
        '''
        del UserInput.__listeners[(pygame.QUIT, None)][id]
    
    @staticmethod
    def onKeyDown(callback, key):
        '''
            Purpose    : Calls the given callback whenever the specified keys are pressed
            Parameters : (function)    callback := The function to call on key down
                         (pygame.keys) keys     := The key pressed to call the function
            Return     : (tuple) The list of ids representing listener (for removal)
        '''
        return UserInput.__addListener(pygame.KEYDOWN, key, callback) 

    @staticmethod
    def onAnyKeyDown(callback):
        '''
            Purpose    : Calls the given callback whenever any key is pressed
            Parameters : (function) callback := The function to call on key down
            Return     : (int) The id representing the listener (for removal)
        '''
        return UserInput.__addListener(pygame.KEYDOWN, None, callback)

    @staticmethod 
    def removeKeyDown(key, id):
        '''
            Purpose    : Remove the given ids from the key down call
            Parameters : (pygame.key) key := The key that calls when pressed 
                         (int)        id  := The id to remove from the listener
            Return     : (None)
        '''
        del UserInput.__listeners[(pygame.KEYDOWN, key)][id]
    
    @staticmethod 
    def removeAnyKeyDown(id):
        '''
            Purpose    : Remove the given id from the any key down call
            Parameters : (int) id := The id of the listener to remove
            Return     : (None)
        '''
        del UserInput.__listeners[(pygame.KEYDOWN, None)][id]

    @staticmethod
    def onKeyUp(callback, key):
        '''
            Purpose    : Calls the given function whenever a key is released
            Parameters : (function)   callback := The function to be called
                         (pygame.key) key      := The key which activate when released
            Return     : (tuple) List of the IDs representing the listeners
        '''
        return UserInput.__addListener(pygame.KEYUP, key, callback) 
    
    @staticmethod 
    def onAnyKeyUp(callback):
        '''
            Purpose    : Calls the given function whenever any key is released
            Parameters : (function) callback := The function to be called
            Return     : (int) The id representing the listener
        '''
        return UserInput.__addListener(pygame.KEYUP, None, callback)

    @staticmethod 
    def removeKeyUp(key, id):
        '''
            Purpose    : Removes the given listeners listening for a specific key
            Parameters : (pygame.key) key := The key which the listeners were listening for
                         (int)        id  := The listener to remove
            Return     : (None)
        '''
        
        del UserInput.__listeners[(pygame.KEYUP, key)][id]
    
    @staticmethod
    def removeAnyKeyUp(id):
        '''
            Purpose    : Removes the given listeners listening for any key
            Parameters : (int)  id  := The listeners to remove
            Return     : (None)
        '''
        del UserInput.__listeners[(pygame.KEYUP, None)][id]

    @staticmethod
    def onMouseDown(callback, button):
        '''
            Purpose    : Listens for the mouse button to be pressed and calls the callback
            Parameters : (function)      callback := The function to call when clicked
                         (pygame.button) buttons  := The button to listen for
            Return     : (tuple) The list of the ids for the listeners
        '''
        return UserInput.__addListener(pygame.MOUSEBUTTONDOWN, button, callback)

    @staticmethod 
    def onAnyMouseDown(callback):
        '''
            Purpose    : Listens for any mouse click
            Parameters : (function) callback := The function to call when clicked
            Return     : (int) The id of the listener
        '''
        return UserInput.__addListener(pygame.MOUSEBUTTONDOWN, None, callback)
    
    @staticmethod 
    def removeMouseDown(button, id):
        '''
            Purpose    : Removes listeners for specific mouse clicks
            Parameters : (pygame.button) button := The button to listen for
                         (int   )        id     := The id of the one to remove
            Return     : (None)
        '''
        del UserInput.__listeners[(pygame.MOUSEBUTTONDOWN, button)][id]

    @staticmethod
    def removeAnyMouseDown(id):
        '''
            Purpose    : Removes listeners for any mouse click
            Parameters : (int) id := The id of the one to remove
            Return     : (None)
        '''
        del UserInput.__listeners[(pygame.MOUSEBUTTONDOWN, None)][id]

    @staticmethod
    def onMouseUp(callback, button):
        '''
            Purpose    : Listens for the specific mouse button to be released and calls the callback
            Parameters : (function)         callback := The function to call when released
                         (pygame.button) buttons  := The buttons to listen for
            Return     : (tuple) The list of the ids for the listeners
        '''
        return UserInput.__addListener(pygame.MOUSEBUTTONUP, button, callback) 
                     
    @staticmethod
    def onAnyMouseUp(callback):
        '''
            Purpose    : Listens for any mouse button release
            Parameters : (function) callback := The function to call when released
            Return     : (int) The id of the listener
        '''
        return UserInput.__addListener(pygame.MOUSEBUTTONUP, None, callback)
    
    @staticmethod
    def removeMouseUp(button, id):
        '''
            Purpose    : Removes listeners for specific mouse release
            Parameters : (pygame.button) button := The button to listen for
                         (int)           id     := The id of the one to remove
            Return     : (None)
        '''
        del UserInput.__listeners[(pygame.MOUSEBUTTONUP, button)][id]

    @staticmethod 
    def removeAnyMouseUp(id):
        '''
            Purpose    : Removes listeners for any mouse release
            Parameters : (int) id := The id of the one to remove
            Return     : (None)
        '''
        del UserInput.__listeners[(pygame.MOUSEBUTTONUP, None)][id]

    @staticmethod
    def onMouseMove(callback):
        '''
            Purpose    : Listens for mouse movement and calls the callback
            Parameters : (function)  callback := The function to call when released
            Return     : (int) The id of the listener
        '''
        return UserInput.__addListener(pygame.MOUSEMOTION, None, callback)

    @staticmethod
    def removeMouseMove(id):
        '''
            Purpose    : Removes listeners for mouse movement
            Parameters : (int) id := The id of the one to remove
            Return     : (None)
        '''
        del UserInput.__listeners[(pygame.MOUSEMOTION, None)][id]

    ''' HELPERS '''

    @staticmethod
    def __addListener(eventType, eventValue, callback):
        '''
            Purpose    : Adds the given listener
            Parameters : (pygame.event.type)      eventType  := The type of event to listen for
                         (pygame.event.key | 
                             pygame.event.button) eventValue := The specific event value
                         (function)               callback   := The function call
            Return     : (None)
        '''
        id = None
        eventKey = (eventType, eventValue)

        if eventKey not in UserInput.__listeners:
            UserInput.__listeners[eventKey] = dict() 
        listeners = UserInput.__listeners[eventKey]

        id = UserInput.__id 
        UserInput.__id += 1
        
        listeners[id] = callback
        return id
    
    @staticmethod
    def __handle(eventType, eventValue, args = None):
        '''
            Purpose    : Calls the callback
            Parameters : (pygame.event.type)      eventType  := The type of event to listen for
                         (pygame.event.key | 
                             pygame.event.button) eventValue := The specific event value
                         (function)               callback   := The function call
            Return     : (None)
        '''
        eventKey = (eventType, eventValue)
        
        if eventKey not in UserInput.__listeners:
            return
        listeners = UserInput.__listeners[eventKey]

        if args:
            for callback in listeners.values():
                callback(*args)
        else: 
            for callback in listeners.values():
                callback()

    ''' UPDATER '''

    @staticmethod
    def check():
        '''
            Purpose    : Checks the button inputs
            Parameters : (None)
            Return     : (None)
        '''
        for event in pygame.event.get():
            value = None
            args  = None

            if (event.type == pygame.QUIT):
                pass
            elif (event.type == pygame.MOUSEBUTTONDOWN):
                # print(UserInput.__listeners)
                value = event.button
                args = (event.pos, )
            elif (event.type == pygame.MOUSEBUTTONUP):
                value = event.button
                args = (event.pos, )
            elif (event.type == pygame.MOUSEMOTION):
                args = (event.rel, event.pos)
            elif (event.type == pygame.KEYDOWN):
                value = (event.key, )
            elif (event.type == pygame.KEYUP):
                value = (event.key, )

            if value:
                UserInput.__handle(event.type, value, args)
            UserInput.__handle(event.type, None, args)


        
