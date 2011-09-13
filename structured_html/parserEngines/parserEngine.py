class ParseDefinition(object):
    def __init__(self, nodeType):
        '''
        Initializes ParseDefinition.
        @param nodeType: Type of objectInterface node to be created when parsing.
        @type nodeType: ObjectInterface node type.
        '''
        self.nodeType= nodeType

class ParserBlock(object):
    parseDefintions= []
    
    def AddParseDefinition(self, parseDefinition):
        '''
        Adds ParseDefinition to ParserBlock.
        @param parseDefinition: Definition to add to parser block
        @type parseDefinition: ParseDefinition
        '''
        self.parseDefintions.append(parseDefinition)
    
    def Parse(self, frame):
        '''
        Parses webFrame using parseDefinition. new objectInterface is created.
        @param frame: Frame to parse
        @type frame: webFrame
        @return: Interface to page.
        @type return: objectInterface.
        '''
        pass
