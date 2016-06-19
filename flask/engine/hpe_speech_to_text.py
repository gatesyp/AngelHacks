from havenondemand.hodclient import *

class useHaven():

        obj={
  "actions": [
    {
      "result": {
        "document": [
          {
            "content": "ok in today's video we're going to go over kinetic energy and here we have our definition of kinetic energy and object that is in motion and that's what kinetic means In Motion object that it's in motion has the ability to do work that is it has the ability to apply a force over a distance and therefore we say it has energy the energy that an object possesses an object has glued to their motion is called kinetic energy and that's often how we just simplified definition we often say the definition of kinetic energy is the energy of motion something has to be moving to have kinetic energy this is the equation we use for kinetic energy to calculate kinetic energy K E is equal to one have M V squared am stands for the mass V stands for the velocity and you're going to where the velocity and only the velocity with one half times the mass times the velocity squared it doesn't matter in what order you put those three terms into your calculator because it's all multiplication but you have to swear just the velocity one half and the square and when we do that we get Jules the answer that you're going to get the units are going to be in jewel because Jules is the unis for energy at work now let's look at the relationship between the Mass and the kinetic energy and the velocity and the kinetic energy and we can see that the mass is directly proportional to me that the kinetic energy is directly proportional to the mass now what do we when we say it's directly proportional that means if we double the mass or in any case we increase the mass and the kinetic energy will also double if we decrease the Mass and the kinetic energy is going to decrease so when we say directly proportional we mean as one thing increases like the mass than the other thing is also going to increase the kinetic energy so mass increases kinetic energy increases mass decreases kinetic energy decreases now one of the most interesting things about the kinetic energy is its relationship to the velocity or to the velocity squared because it is squared and therefore we say that the kinetic energy is directly proportional to the square of the speed or the square of the loss of tea and going to try and show you what we mean by that because it is significant well we have here is we have four different philosophies this is going to be kind of our ground velocity is going to be our base philosophy five meters per second that is going to be our base that we're going to use and then we're going to compare the other three two that come kinetic energy the object passed with twenty five years for second and we don't know the last because ten is the double five in Triple A Las The Triple Five is fifteen Democratic washable and are going to get twenty years for second ok now we calculate the kinetic energy no I didn't give you a mass and when I like to do these problems let's just choose some nice round number that doesn't really matter what lastly use one kilogram ten kilograms a hundred you could use three hundred and forty point six two mm a little easier to take a nice round number so that we can see their relationship to the velocity and the kinetic energy and I believe I chose one hundred kilograms so we think Katie is one half can be squared means the K in this case is one half point five same thing as one half right time's one hundred kilograms times by square which of course is twenty by twenty by one hundred and twenty five hundred and that is twelve hundred and fifty so an object that has the mass hundred kilograms of twenty five meters per second with twelve hundred and fifty jewels kinetic energy now we're going to double the velocity to ten and what is going to happen to the kinetic energy because the squared so let's see now are going to double we still have ten hit with double meat double the loss that ended the square that so ten times a hundred times one half is going to be five thousand and that shows you that when you double the velocity because the kinetic energy is directly proportional to the square of the velocity below is the velocity goes up by a factor for a triple into the same thing we see that it goes up to the kinetic energy increases we triple the velocity to eleven thousand two hundred and fifty which means you might notice that is nine times for you should notice is going to be sixteen times higher ok so you'll notice it's the square of velocity so if we double the loss the square to get for four times where this you get nine squares sixteen this is significant when you're driving a car has practical applications because means every time you double your speed ok when you double your speed that means this could take you four times as long or four times the distance to stop because the brakes friction with the Roadhouse to four times as much energy and this means is going to be nine times as long and this may take you sixteen times distance stop if you're going twenty meters per second which is four times more than five meters per second ok so that shows you the relationship between the square of the velocity and the kinetic energy ok going to fret now for kinetic energy in the next video which you can click the link to write here you can see some examples that were going to do or use kinetic energy and the work energy theorem to solve some problems so thank you very much for watching I hope you found helpful if you did please not give me a nice cause of calm in the comment section below he and his thumbs up down also ok thanks for watching and we'll see you in the next video"
          }
        ]
      },
      "status": "finished",
      "action": "recognizespeech",
      "version": "v1"
    }
  ],
  "jobID": "w-eu_0f3dbf91-1608-4cbc-a8ca-9f5a817e1a4a",
  "status": "finished"
}
        client=None
        def __init__(self):
                self.client = HODClient("f08c8fef-327f-41a9-96d6-7a4f6148f94d", version="v1")
                print "calling speech2text API"

        def speech_text(self):
                # response_async= self.client.post_request({'file': 'badrecording.wma'}, HODApps.RECOGNIZE_SPEECH, async=True)
                # jobID = response_async['jobID']
                # response1 = self.client.get_job_status(jobID)
                # response2 = self.client.get_job_result(jobID)
                # print response2
                # return response2

		return self.obj

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
