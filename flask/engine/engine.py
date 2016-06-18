from use_alch_api import alchemy
from find_page import findPage
from bs4 import BeautifulSoup
from search import findInfo
from hpe_speech_to_text import useHaven

	
class Engine():
    def __init__(self):
        print ("created engine object")
        
    def execute(self, filename):
        hpe=useHaven()
        json=hpe.speech_text()
        text=json["document"][0]["content"]
        #["actions"][0]["result"]
        keyword_array=hpe.analyze_content(text)
        
        # keyword_array=alchemy().use_api(c2)
        searching=findPage()
        maxpage=searching.find_page(keyword_array)
        find=findInfo(maxpage)
        chapter = find.find_chapter()
        section = find.find_section()



# myEng = Engine()
# myEng.execute("short.html")
