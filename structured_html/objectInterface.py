class Node(object):
    address= None

    def GetAttributes(self):
        pass

    def GetAttributeType(self, name):
        pass

    def __getattr__(self, item):
        pass

    def __setattr__(self, item, value):
        pass

class Attribute(object):
    type= None
    name= None
    webElement= None

class ListAttribute(Attribute):
    nodes= []

    def __get__( self, instance, owner ):
        pass

class TextAttribute(Attribute):
    def __get__( self, instance, owner ):
        pass

class PictureAttribute(Attribute):
    def __get__( self, instance, owner ):
        pass
    
class InputMethod(object):
    def setValue(self, *args):
        pass

class TextInputMethod(InputMethod):
    def setValue(self, *args):
        self.webElement.setValue(args[0])

class ClickInputMethod(InputMethod):
    def setValue(self, *args):
        self.webElement.click()
        
class OptionInputMethod(InputMethod):
    def setValue(self, *args):
        self.webElement.setValue(args[0])

class InputAttribute(Attribute):
    def __init__(self, inputMethod):
        self.inputMethod= inputMethod
        
    def setValue(self, *args):
        return self.inputMethod.setValue(args)
    
    def getValue(self):
        return self.inputMethod.getValue()
    
class SimpleInputAttribute(InputAttribute):
    pass

class ParseInputAttribute(InputAttribute):
    '''
    Uses parserBlock to create interface for the
    same page or for new page.
    '''
    parserBlock= None
    webEngine= None
    newPage= True
