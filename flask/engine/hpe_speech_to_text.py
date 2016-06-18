from havenondemand.hodclient import *

class useHaven():
        client=None
        def __init__(self):
                self.client = HODClient("f08c8fef-327f-41a9-96d6-7a4f6148f94d", version="v1")
                print "calling speech2text API"

        def speech_text(self):
                response_async= self.client.post_request({'file': 'badrecording.wma'}, HODApps.RECOGNIZE_SPEECH, async=True)
                jobID = response_async['jobID']
                response1 = self.client.get_job_status(jobID)
                response2 = self.client.get_job_result(jobID)
                print response2
                return response2

        def analyze_content(self,text):
                response_async=  self.client.post_request({'text': text}, HODApps.EXTRACT_CONCEPTS, async=True)
                jobID = response_async['jobID']
                response1 = self.client.get_job_status(jobID)
                response2 = self.client.get_job_result(jobID)
                print response2
                for items in response2['concepts']:
                        array=items['concept']

                return array            
                



#response = client.get_job_status(jobID)

#print response
