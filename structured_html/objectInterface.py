class Node(Object):
    address= None

    def GetAttributes(self):
        pass

    def GetAttributeType(self, name):
        pass

    def __getattr__(self, item):
        pass

    def __setattr__(self, item, value):
        pass

class Attribute(Object):
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

class LinkAttribute(Attribute):
    def __get__( self, instance, owner ):
        pass

class InputAttribute(Attribute):
    def __get__( self, instance, owner ):
        pass
    def __set__(self, instance, value):
        pass

class RemoteLinkAttribute(Attribute):
    linkAddress= None
    parserDefinition= None
    parserEngine= None
    webEngine= None

    def __get__( self, instance, owner ):
        pass
