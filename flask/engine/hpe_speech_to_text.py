from havenondemand.hodclient import *
client = HODClient("f08c8fef-327f-41a9-96d6-7a4f6148f94d", version="v1")

response_async=  client.post_request({'file': 'badrecording.wma'}, HODApps.RECOGNIZE_SPEECH, async=True)

jobID = response_async['jobID']

response1 = client.get_job_status(jobID)

response2 = client.get_job_result(jobID)
print response2


#response = client.get_job_status(jobID)

#print response