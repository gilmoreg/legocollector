''' Utilities for testing '''
import json


def decode_json(response):
    ''' Decode JSON from Flask response '''
    return json.loads(response.data.decode('utf8'))

def post_json(client, url, json_dict):
    '''Send dictionary json_dict as a json to the specified url '''
    response = client.post(url, data=json.dumps(json_dict), content_type='application/json')
    print(response)
    return response
