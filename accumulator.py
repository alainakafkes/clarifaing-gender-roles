# Clarifai Image Tag Accumulator
# to run, follow instructions on: https://github.com/Clarifai/clarifai-python

import json
from collections import defaultdict
from clarifai.client import ClarifaiApi
clarifai_api = ClarifaiApi()

# initialize tag dictionary for tags and their frequencies
d = defaultdict(int)
taglist = []
iter = 0

# read and process each url
with open("imglist.txt") as f:
    imglist = f.readlines()

# get tags using clarifai, add tags to taglist
for line in imglist:
    result = clarifai_api.tag_image_urls(line.rstrip('\n'))
    tags = result['results'][0]['result']['tag']['classes']
    for i in range(0,len(tags)):
        if type(tags[i]) is str:
            taglist.append(tags[i])
    print("next iter:" + str(iter))
    iter += 1

# convert taglist to dictionary
for x in range(0,len(taglist)):
    d[taglist[x]] += 1

# print dictionary
for w in sorted(d, key=d.get, reverse=True):
    print(w, d[w])
