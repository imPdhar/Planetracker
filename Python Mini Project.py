#!/usr/bin/env python
# coding: utf-8

# In[7]:


import os
from twilio.rest import Client
from opensky_api import OpenSkyApi
account_sid = 'AC697d49374d8ad50ca9def147ad75fcef'
auth_token = 'bd3a17e965ed68c045fc1fb74c82e1ec'
# bbox = (min latitude, max latitude, min longitude, max longitude)
api = OpenSkyApi()
states = api.get_states(bbox=(12.9050, 13.3191, 77.4656, 77.7588))
hello=[]
for s in states.states:
    stateplane="(%r, %r, %r, %r)" % (s.callsign, s.latitude, s.icao24, s.velocity)
    hello.append(stateplane)
    #print(hello)
    listToStr = ''.join(map(str, hello))
    print(listToStr)  
client = Client(account_sid, auth_token)
message = client.messages                 .create(

                     body=listToStr,
                     from_='+12516072280',
                     to='+918867295459'
                )
    
    
    


# In[ ]:


#BSK LOCATION (12.9050, 13.3191, 77.4656, 77.7588)

