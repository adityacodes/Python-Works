
#  GET latitude and longitude using Google Geocode API

import httplib2
import json

def getGeocodeLocation(inputString):
	google_api_key = "[YOUR_API_KEY_HERE]"
	locationString = inputString.replace(" ", "+")
	url	= ('https://maps.googleapis.com/maps/api/geocode/json?address=%s&key=%s'%(locationString, google_api_key))
	h = httplib2.Http()
	response, content = h.request(url, 'GET')
	# content = h.request(url, 'GET')
	result = json.loads(content)
	latitude =  result['results'][0]['geometry']['location']['lat']
	longitude = result['results'][0]['geometry']['location']['lng']
	print 'Latitude : ' + str(latitude) + "  " + 'Longitude : ' + str(longitude)

getGeocodeLocation("Upper Police Colony, Tulasipur, Cuttack, Odisha")