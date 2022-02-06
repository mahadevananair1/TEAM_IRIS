import firebase,time,yagmail
from twilio.rest import Client
# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid ='AC6a983c5e17d02271f8e08d1086d1308d'
auth_token ='2db53e2b45bd98d84587c28610749031'
client = Client(account_sid, auth_token)
firebase = firebase.FirebaseApplication('https://team-iris-default-rtdb.firebaseio.com/', None)
while True:
    data= firebase.get('/115207','')
    if data['Alarm'] == 'True':
        call = client.calls.create(
                        url='https://handler.twilio.com/twiml/EHf3dfb6eac24dc7a9d5f459d376f6186a',
                        to='+916282143473',
                        from_='+18597245468'
                    )
        print("Made the call",call.sid)
        time.sleep(5)
        loc = 'https://www.google.com/maps/search/?api=1&query='+str(data['Lat']) +','+ str(data['Long'])
        message = client.messages.create(   
                              body=f'Hi I am {data["Name"]}, I have an emergency situation.. Please help me, I am here {loc}',      
                              to='+916282143473',
                                from_='+18597245468'

                          )
        firebase.put('/115207','Alarm','False') 
        print("Made the message",message.sid)
        try:
            #initializing the server connection
            yag = yagmail.SMTP(user='dpservice200@gmail.com', password='Soorajsivadas767*')
            #sending the email
            yag.send(to=data['Contact1Email'], subject='Emergency ❗❗❗❗', contents=f'Hi I am {data["Name"]}, I have an emergency situation.. Please help me, I am here {loc}')
            print("Email sent successfully")
        except:
            print("Error, email was not sent")
        print("Session Completed :)")
# Download the helper library from https://www.twilio.com/docs/python/install







    