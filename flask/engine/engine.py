from use_alch_api import alchemy
from find_page import findPage
from bs4 import BeautifulSoup
from search import findInfo
from hpe_speech_to_text import useHaven
from generate import getContent 
import json
import flask

	
class Engine():
    def __init__(self):
        print ("created engine object")
        
    def execute(self, filename):
	hpe=useHaven()
	json=hpe.speech_text()
	text=json['actions'][0]['result']["document"][0]["content"]
        #["actions"][0]["result"]
        keyword_array=hpe.analyze_content(text)
        
        # keyword_array=alchemy().use_api(c2)
        print "keyword_array reached"
        searching=findPage()
        print "findPage() reached"
#        maxpage=searching.find_page(keyword_array)
#        find=findInfo(maxpage)
#        chapter = find.find_chapter()
#        section = find.find_section()
	# make a getContent object
	generation = getContent()
	exercises = generation.get_questions('Kinetic Energy')
	vids = generation.get_videos('Kinetic Energy')
	summary = generation.get_smry("test.txt")
        #  TODO take all these variables and create one JSON object
        #  text, keyword_array, chapter, section, exercises, vids, summary
        outline = {
            'exercises': exercises,
            'vids': vids, 
            'summary': summary
        }
        return flask.jsonify({'data' : outline})










# myEng = Engine()
# myEng.execute("short.html")
