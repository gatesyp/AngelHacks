from bs4 import BeautifulSoup
#from use_alch_api import keyword_array
import re

class findPage():
    soup = None
    def __init__(self):
        print "created a findPage object"
        self.soup = BeautifulSoup(open("short.html"),"html.parser") #use test.html instead of short.html for full page

    def find_page(self, input):
        hold_values =[]
        occurances=[0]*1000
        
        for search_terms in input:
            i=0
            for tag in self.soup.find_all(text=re.compile(search_terms)):#searches for the key word, everytime the keyword 
                                       #is found it stores the <a"filler" /a> in the hold_values array
             hold_values.append((tag))

    

        for values in hold_values:
            page_number= hold_values[i].findPrevious('a')['name']#goes through array and just picks out the page number
            page_number=int(page_number)#converts page number from unicode to int
            occurances[page_number]=occurances[page_number]+1#everytime that word is found increment that page number's value in the array
    # print occurances[page_number]
            i=i+1

        max_occurances=max(occurances) #finds largest value in list
        max_occurances_index=occurances.index(max_occurances) #finds the index of that value (which is the page number)
        print max_occurances_index
        max_occurances_index=str(max_occurances_index) #actual page is max_occurances-25
        return max_occurances_index





