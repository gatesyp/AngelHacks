from alchemyapi import AlchemyAPI
#from HARDCODE import c2

class alchemy:
	def __init__(self):
		print "created a alchemy object"

	def use_api(self, input):
		keyword_array=[]
		alchemyapi = AlchemyAPI()
		response = alchemyapi.keywords("text", input)
		for keyword in response["keywords"]:
			#print keyword["text"].encode('utf=8')
			keyword_array.append(keyword["text"].encode('utf=8'))
		return keyword_array

