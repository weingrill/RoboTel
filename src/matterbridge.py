# https://mattermost.com/blog/mattermost-integrations-incoming-webhooks/
# see also https://mattermost.com/blog/mattermost-integrations-mattermost-api/
import requests
# the part where we read the actual temperatures is  replaced by the next line
temperature= 3.14159265358979323846
   
#actual code for sending
headers = {'Content-Type': 'application/json',}
values = '{ "text": "The temperature of the fridge is now '+str(temperature).replace(".",",")+' degrees Celcius"}'
response = requests.post('https://{your-mattermost-site}/hooks/xxx-generatedkey-xxx', headers=headers, data=values) 
