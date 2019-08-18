import requests
import json


# if there are param1 do a get call with parameters, if there are no extra paramseters do a get call
# There is no need to a get request with just headers.
#Request combinations:
#headers params - ok
#headers data - ok
#headers params data
#params - ok
#data - ok
#empty - ok
def make_request(**kwargs):
    try:
        apiUrl = kwargs["apiUrl"]
    except:
        return ({"testing_apis function": "The main url for the API is missing"})

    try:
        apiEndpoint = kwargs["apiEndpoint"]
        # Add an endpoint to the api
        fullAPIUrl = apiUrl + apiEndpoint
    except:
        return ({"testing_apis": "The API endpoint for te API is missing"})

    try:
        data1 = kwargs["data1"]
        result = requests.get(fullAPIUrl, data=json.dumps(data1))
    except:
        return ({"testing_api": "Missing API data"})

    
    if result.status_code in (400, 401, 402, 403, 404):
        return result

    return result.json()
