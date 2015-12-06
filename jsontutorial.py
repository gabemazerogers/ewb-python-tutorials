import hashlib, random, requests
import json
api_key = hashlib.sha224( str(random.getrandbits(256)) ).hexdigest();
print api_key;

url = 'http://api.rottentomatoes.com/api/public/v1.0/lists/movies/box_office.json?apikey=%s&limit=1', api_key

params = dict(
	country = 'USA',
	limit = 10)
resp = requests.get(url = url, params = params)
data = json.loads(resp.text)
print data

#This isn't working right now, I'll try it again another time. Sorry pals.