''' 
    Utilities for testing
    Some adapted from https://serge-m.github.io/testing-json-responses-in-Flask-REST-apps-with-pytest.html
'''
import json
import jwt
import traceback
from os import environ
from bs4 import BeautifulSoup


def create_jwt(user_id):
        ''' Create JSON Web Token and decode to string '''
        token = jwt.encode(
            {'user': user_id},
            environ['JWT_SECRET'],
            algorithm='HS256')
        return token.decode('utf-8')


def decode_json(response):
    ''' Decode JSON from Flask response '''
    return json.loads(response.data.decode('utf8'))

def post_json(client, url, json_dict):
    '''Send dictionary json_dict as a json to the specified url '''
    response = client.post(url, data=json.dumps(json_dict), content_type='application/json')
    print(response)
    return response

bottlenose_mock_success = BeautifulSoup('''
    <?xml version="1.0" ?>
    <html>
        <body>
            <itemsearchresponse xmlns="http://webservices.amazon.com/AWSECommerceService/2013-08-01">
                <item>
                    <detailpageurl>https://amazon.com/test_setname/dp/TESTASIN00</detailpageurl>
                    <itemattributes>
                        <title>Test Set Title</title>
                    </itemattributes>
                    <mediumimage>
                        <url>https://images-na.ssl-images-amazon.com/images/I/Test._SL160_.jpg</url>
                    </mediumimage>
                </item>
            </itemsearchresponse>
        </body>
    </html>
''', 'lxml')

bottlenose_mock_empty = BeautifulSoup('''
    <?xml version="1.0" ?>
    <html>
        <body>
            <itemsearchresponse xmlns="http://webservices.amazon.com/AWSECommerceService/2013-08-01">
                <items>
                    <request>
                        <errors>
                            <error>
                                <code>AWS.ECommerceService.NoExactMatches</code>
                                <message>We did not find any matches for your request.</message>
                            </error>
                        </errors>
                    </request>
                    <totalresults>0</totalresults>
                    <totalpages>0</totalpages>
                </items>
            </itemsearchresponse>
        </body>
    </html>
''', 'lxml')