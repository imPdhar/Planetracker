import os
from twilio.rest import Client     #ImportingSMSAPI
from opensky_api import OpenSkyApi  #ImportingDataAPI
account_sid = 'Acquired_sid' #DeclareSMSAPI’sSID
auth_token = 'AcquiredAuthToken' #DeclareSMSAPI’sAuthToken
api = OpenSkyApi()#CallingDataAPI
states = api.get_states(bbox=(45.8389, 47.8229, 5.9962, 10.5226)) #BoundingBoxForRequiredLocation
hello=[] #DeclareAnEmptyList
for s in states.states:
    stateplane="(%r, %r, %r)" % (s.callsign, s.geo_altitude, s.vertical_rate,)#AcquireLiveData
    hello.append(stateplane) #AppendDataToTheList
    listToStr = ''.join(map(str, hello))#ConvertListToString
    #print(listToStr)  
client = Client(account_sid, auth_token)#CallingSMSAPI
message = client.messages \
                .create(

                     body=listToStr, #AssignData
                     from_='+1xxxxxxxx', #AssignFromNumber
                     to='+[Country Code][User’s Cell-number]'  #AssignToNumber
                )    
