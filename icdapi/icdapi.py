import requests

token_endpoint = 'https://icdaccessmanagement.who.int/connect/token'
client_id = 'bce138cd-2d1f-4056-94c1-e856711323aa_222cf1dc-a781-4d6f-8e74-0cd1d443ceb2'
client_secret = 'fZbKETejwxpP2rnrCjuH2TAXHSKqcldbpfh00m8U5tI='
scope = 'icdapi_access'
grant_type = 'client_credentials'

# get the OAUTH2 token

# set data to post
payload = {'client_id': client_id,
           'client_secret': client_secret,
           'scope': scope,
           'grant_type': grant_type}

# make request
r = requests.post(token_endpoint, data=payload, verify=False).json()
token = r['access_token']

# access ICD API

uri = 'https://id.who.int/icd/entity'

# HTTP header fields to set
headers = {'Authorization': 'Bearer ' + token,
           'Accept': 'application/json',
           'Accept-Language': 'en',
           'API-Version': 'v2'}

# make request
r = requests.get(uri, headers=headers, verify=False)

# print the result
print(r.text)
print(r.json())
print(r.content)
