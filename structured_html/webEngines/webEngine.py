from xml.dom import Node

class HtmlNode(Node):
    pass

class HtmlAttributeNode(HtmlNode):
    def __init__(self):
        self.nodeType= Node.ATTRIBUTE_NODE
    
class HtmlNodeElement(HtmlNode):
    '''
    HtmlNode child classes must implement dom functions,
    and functions defined in this class.
    '''
    
    def __init__(self):
        self.nodeType= Node.ELEMENT_NODE
        
    def getElementsByXpath(self, xpath):
        '''
        TODO: Implement xpath using python native xpath.
        @param xpath: xpath
        @type xpath: string
        '''
        
    def getElementById(self, id):
        '''
        TODO: Implement using dom.
        @param id: id attribute of element
        @type id: string
        '''
        pass
    
    def getElementsByName(self, name):
        '''
        TODO: Implement using xpath.
        @param name: name attribute of element.
        @type name: string
        '''
        pass
    
    def elementType(self):
        '''
        Type of an element used for data input,
        like image, option selector, text.
        '''
        pass
    
    def setValue(self, value):
        '''
        Sets value to element.
        @note: On implementations like selenium this is supposed to get done only
               on interactive elements.
        @param value: Value to set
        @type value: unknown yet
        '''
        pass
    
    def click(self):
        '''
        Clicks element.
        '''
        pass
    
class webPage(object):
    def getMainFrame(self):
        '''
        Gets main frame.
        '''
        pass
    
    
    def navigate(self, url):
        pass

class webFrame(object):
    '''
    The root frame is MainFrame.
    '''
    def getChildFrame(self, id):
        '''
        Gets child frame by id.
        @param id: Id of child frame.
        @type id: Id of frame like number or name.
        '''
        pass