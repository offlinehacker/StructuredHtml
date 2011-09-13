import re

from parserEngine import ParserBlock, ParseDefinition

class XpathParseDefinition(ParseDefinition):
    def __init__(self, xpaths, klas):
        self.xpaths= xpaths
        self.klas= klas
        
    def SliceXpathByFrames(self, xpath):
        '''
        Slices xpath where are iframe elements.
        @param xpath: XPath string.
        @type xpath: string
        '''
        #TODO: better splitting method must be implemented
        results= re.split("\\iframe.+\\?", xpath)
        outResults= []
        outResults.append(results[0])
        for x, result in enumerate(results):
            if result=="" or x==0: continue
            else:
                outResults.append("\\" + result)
               
        return outResults

class XpathParserBlock(ParserBlock):
    def __init__(self, *args):
        ParserBlock.__init__(self, args)
        
    def Parse(self, frame):
        #Go through all ParseDefinitions
        for parseDefinition in self.parseDefintions:
            #Go through all xpaths and try one that works.
            elements= None
            for xpath in parseDefinition.xpaths:
                elements=frame.getElementsByXpath(xpath)
                if elements: break
                
                element= elements[0]
                
            