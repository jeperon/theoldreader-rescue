import requests

print('Fetching access token')
r = requests.post('https://theoldreader.com/accounts/ClientLogin', 
  data = {'client':'theoldreader-rescue', 
          'accountType' : 'HOSTED_OR_GOOGLE',
          'service' : 'reader',
          'Email' : 'XXXXX',
          'Passwd' : 'YYYYYYY'})

if (not r.ok):
    print('Could not obtain access token')
    quit()

token = r.text.splitlines()[2][5:]
print('Token is: {}'.format(token))

# Get user info
headers = { 'Authorization' : 'GoogleLogin auth={}'.format(token) }
user_info = requests.get("https://theoldreader.com/reader/api/0/user-info?output=json",
    headers = headers)

if not user_info.ok:
    print('Could not fetch user info')
    quit()

print('User name: {}'.format(user_info.json()['userName']))

# Get item list
item_response = requests.get("https://theoldreader.com/reader/api/0/stream/items/ids?output=json&s=user/-/state/com.google/reading-list&n=10000&ot=1591622581",
    headers = headers)

if not item_response.ok:
    print('Could not load item list')
    quit()

item_list = item_response.json()['itemRefs']

print('item count: {}'.format(len(item_list)))

def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

item_ids = ["tag:google.com,2005:reader/item/{}".format(v['id']) for v in item_list]

batches = chunks(item_ids, 100)

for batch in batches:

    data = { 'i' : batch, 'r' : 'user/-/state/com.google/read'}
    
    mark_unread_response = requests.post('https://theoldreader.com/reader/api/0/edit-tag',
        headers = headers,
        data = data)
    
    print('Final result: {}'.format(mark_unread_response.text))

