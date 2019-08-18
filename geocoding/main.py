from request import make_request
from credentials.credentials import my_key, my_address


#header = {"header1": {"X-API-KEY": key, "Content-Type": ctype}}
apiUrl = {"apiUrl": "https://eu1.locationiq.com/v1/"}
apiEndpoint = {"apiEndpoint": "search.php"}
params =  {"params1":{'key': my_key,
    'q': my_address,
    'format': 'json'}}
result = make_request(**apiUrl, **apiEndpoint, **params)
print(result)


