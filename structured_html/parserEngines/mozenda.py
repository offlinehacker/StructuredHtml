from io import FileIO
from lxml import objectify

from xpathParserEngine import XpathParserBlock
    
class MozendaParser(object):
    '''
    Parses whole mozenda files and generates
    many parser blocks for differnet pages.
    Mozenda's capture program is best in business,
    but still very bad. We use mozenda, just because
    there is no any other simple alternative. But i'm
    gonna eat you alive mozenda in matter of year, thats
    not how you should do business.
    '''
    def MozendaParser(self, filepath):
        self.f= FileIO(filepath)
        self.document= objectify.parse(self.f).getroot()
        
        try:
            current_parser_block= None
            for Action in self.document.AgentDefinition.ActionList.Action:
                #We create a new ParserBlock when we see PagePlaceHolder
                if Action.ActionType=="PagePlaceHolder":
                    current_parser_block= XpathParserBlock()
                elif Action.ActionType=="BeginAnchorList":
                    
        except:
            return        
