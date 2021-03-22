import requests

url = 'https://superheroapi.com/api/'
token = '' + '/'
func = 'search/'
supers = ['Hulk', 'Captain America', 'Thanos']
rate_IQ = {}

for name in supers:
    request = requests.get(url + token+ func + name)
    rate_IQ.update({int(request.json()['results'][0]['powerstats']['intelligence']): name})

max_IQ = rate_IQ[max(rate_IQ.keys())]

print(max_IQ)