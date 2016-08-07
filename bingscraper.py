# Bing Image Scraper

with open("bingsecrets.txt") as f:
    secrets = f.readlines()
account_key = secrets[0].rstrip('\n')

import urllib
import requests
from requests.auth import HTTPBasicAuth
import json
import random

def get_pics(keyword="engineer"):
    """ amass pictures by keyword """

    # search url obtained from bing api
    url = "https://api.cognitive.microsoft.com/bing/v5.0/images/search?q=" + keyword + "&count=150&offset=0&mkt=en-us&safeSearch=Moderate"

    # get ~authorized~
    headers = {'Ocp-Apim-Subscription-Key': account_key}

    # get response from search url
    response_data = requests.get(url, headers=headers)

    # decode json-formatted response & save as pomeranians.json
    json_result = response_data.json()
    json_pretty = json.dumps(json_result, indent=4, sort_keys=True)
    with open("results.json","w") as outfile:
        outfile.write(json_pretty)
    outfile.close()

    # create list of content urls
    with open("imglist.txt","w") as outfile:
        for i in range(0,150):
             outfile.write(str(json_result['value'][i]['contentUrl'])+"\n")
    outfile.close()

    return "complete!"
