#!/usr/bin/env python

# githubber.py

import sys
import json
import requests



if __name__ == "__main__":
    username = sys.argv[1]
    response = requests.get('https://api.github.com/users/{}/events'.format(username))
    jsonresponse = json.loads(response.content)
    types = []
    for item in jsonresponse:
        types.append(item['type'])

    print('{} events:'.format(len(types)))
    print(types)

    print('First event was a {} and was at: {}'.format(
                    jsonresponse[0]['type'],jsonresponse[0]['created_at']))

    


