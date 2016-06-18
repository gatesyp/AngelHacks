from bs4 import BeautifulSoup
#from main import soup, max_occurances_index
import re

class findInfo():
        sib=[]
        soup=  BeautifulSoup(open("short.html"),"html.parser")
        def __init__(self,max_index):
                print "created a findInfo object"
                #self.soup = BeautifulSoup(open("short.html"),"html.parser")
                page=self.soup.find(text=re.compile("Page " + max_index))
                span=page.find_parent("div")
                self.sib=span.find_previous_siblings("div")
                


        # def create_max(self,max_occurances_index):
        #       self.soup = BeautifulSoup(open("short.html"),"html.parser")
        #       page=self.soup.find(text=re.compile("Page " + max_occurances_index))
        #       span=page.find_parent("div")
        #       self.sib=span.find_previous_siblings("div")

        def find_section(self):
                print "hi"
                for values in self.sib:
                        children=values.findChild(text=re.compile(r'\d\.\d:|\d\.\d\.'))
                        if children!=None:
                                print children.encode('utf=8')
                                break
        def hello(self):
                print 'die'

        def find_chapter(self):
                for values in self.sib:
                        chapter=values.findChild(text=re.compile(r'Week \d:'))
                        if chapter!=None:
                                print chapter.encode('utf=8')
                                return chapter.encode('utf=8')

#print find_chapter()
        #print find_section
        #print find_chapter
#print children.encode('utf=8')
#dog = findInfo()
#dog.find_section
#print chapter.encode('utf=8')
   
