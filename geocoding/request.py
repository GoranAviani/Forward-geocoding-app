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
def make_request(*args, **kwargs):
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
        params1 = kwargs["params1"]
        try:
            data1 = kwargs["data1"]
            try:
                header1 = kwargs["header1"]
                return requests.get(fullAPIUrl, headers=header1, params=params1, data=json.dumps(data1))
            except:
                return requests.get(fullAPIUrl, params=params1, data=json.dumps(data1))
        except:
            try:
                header1 = kwargs["header1"]
                return requests.get(fullAPIUrl, headers=header1, params=params1)
            except:
                return requests.get(fullAPIUrl, params=params1)
    except:
        pass

    try:
        data1 = kwargs["data1"]
        try:
            header1 = kwargs["header1"]
            return requests.get(fullAPIUrl, headers=header1, data=json.dumps(data1))
        except:
            return requests.get(fullAPIUrl, data=json.dumps(data1))
    except:
        try:
            header1 = kwargs["header1"]
            return requests.get(fullAPIUrl, headers=header1)
        except:
            return requests.get(fullAPIUrl)


#result = make_request(*args, **kwargs)

#return result.json()
