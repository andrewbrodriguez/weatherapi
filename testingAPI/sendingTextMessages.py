from twilio.rest import Client
import requests



#Account SID
#AC03ea2e28eb640deed4843d25f71631ec

#Token
#584f8c9cd1d2fc4c2437422d667c07a5

#Number
#18509309178


account_sid = 'AC03ea2e28eb640deed4843d25f71631ec'
auth_token = '584f8c9cd1d2fc4c2437422d667c07a5'

client = Client(account_sid, auth_token)


r = requests.get('http://api.open-notify.org/astros.json')
people = r.json()
number_iss = people['number']


Message = "The CCP knows your location"
#formulate the message that will be sent
message = client.messages.create(
    #to="+16175993645",
    to="+16175993645",
    from_="+18509309178",
    body=Message)
print(message.sid)