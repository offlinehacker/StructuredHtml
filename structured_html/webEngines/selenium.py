from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from webEngine import *

def SeleniumPage(webPage):    
    def __init__(self, driver, handle):
        '''
        Initializes SeleniumPage.
        @note: SeleniumPage instances with same driver, should not call
               functions concurently.
        @param driver: driver to use with selenium(Firefox, Chromium, etc,...)
        @type driver: WebDriver
        @param handle: Handle of the window, used for window switching.
        @type handle: WeDriver window handle.
        '''
        
        self.driver= driver
        self.handle= handle
    
    def navigate(self, url):
        self._selectWindow()
        self.driver.get(url)
        
    def getMainFrame(self):
        return SeleniumFrame(self, 0)
        
    def _selectWindow(self):
        '''
        Selects current window.
        '''
        
        self.driver.switch_to_window(self.handle)
        
def SeleniumFrame(webFrame):
    def __init__(self, page, frame_id, last_frame_id=[]):
        '''
        Initializes SeleniumFrame.
        @note: This frame is "virtual" pointer to frame. It only stores path to
               frame from top of window, and on every access it must get selected
               again and again.
        TODO: Add support for frame checking, so we don't have to select on every 
               access.
        @param page: web page this frame is in.
        @type page: SeleniumPage
        @param frame_id: name or id of a frame to use.
        @type frame_id: string or integer
        @param last_frame_id: List of parent frames.
        @type last_frame_id: list
        '''
        
        self.page = page
        self.frame_id= frame_id-1
        self.last_frame_id= last_frame_id
        
    def _selectFrame(self):
        '''
        Selects frame this class represents.
        @note: Must be called before every action,
               to be shure we are selecting on correct frame.
        '''
        
        # Before we select frame, we have to select window.
        self.page._selectWindow()
        self.page.driver.switch_to_default_content()
        
        # Traverse all frames to reach frame this class represents.
        for frame_id in self.last_frame_id:
            self.page.driver.switch_to_frame( frame_id )
        
        # If frame id is main frame do nothing, because we are already on top.
        if self.frame_id==-1: return
        
        # Go to sub frame of current frame.
        self.page.driver.switch_to_frame( self.frame_id+1 )
    
    def getChildFrame(self, id):
        # First we must make sure that frame we want actually exists.
        try:
            self._selectFrame()
            self.page.driver.switch_to_frame(id)
        except:
            return None
        
        # Return child frame.
        return SeleniumFrame(self.page, id, self.last_frame_id +  [self.frame_id+1])
        
    def document(self):
        return SeleniumRootNodeElement(self)
    
def SeleniumNodeElement(HtmlNodeElement):
    element= None   
    nodeType= Node.ELEMENT_NODE
    
    def __init__(self, element):  
        self.element = element
        
    def _toHtmlWebElements(self, elements):
        '''
        Converts selenium WebElement list to our representation.
        @param elements: Selenium WebElement list.
        @type elements: WebElement
        '''
        outElements= []
        
        for element in elements:
            outElements.append(SeleniumNodeElement(element))
            
        return outElements
    
    def getElementsByXpath(self, xpath):
        return self._toHtmlWebElements( self.element.find_elements_by_xpath(xpath) )
    
    def getElementById(self, id):
        return SeleniumNodeElement( self.element.find_element_by_id(id) )
    
    def getElementsByName(self, name):
        return self._toHtmlWebElements( self.element.find_elements_by_name(name) )
    
    def tagName(self):
        return self.element.tag_name
    
    def hasAttribute(self, name):
        return self.element.get_attribute(name)
    
    def getAttribute(self, name):
        return self.element.get_attribute(name)
    
    def setValue(self, value):
        # In case we have option element.
        if element.tagName=="option":
            for x, option in enumerate(element):
                if x==value:
                    option.setSelected()
        # We suppouse that we are setting
        # value only to interactive elements.
        else:
            self.element.send_keys(value)
        
    def click(self):
        self.element.click()
       
    def document(self):
        return SeleniumRootNodeElement(self)
    
def SeleniumRootNodeElement(SeleniumNodeElement):
    def __init__(self, frame):
        #Set node type to document
        self.nodeType= Node.DOCUMENT_NODE
        
        self.frame = frame
        driver= frame.page.driver
        
        self.frame._selectFrame()
        #html node is selected
        self.element= driver.find_elements_by_xpath("*")[0]
