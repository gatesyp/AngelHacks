#from generate import getContent as GC
from use_alch_api import alchemy
from HARDCODE import c2
from find_page import findPage
from bs4 import BeautifulSoup
	
class Engine():
    def __init__(self):
        print ("created engine object")
        
    def execute(self, filename):
        keyword_array=alchemy().use_api(c2)
        searching=findPage()
        searching.find_page(keyword_array)
        x=getContent()
        print "hello"
        x.get_questions



