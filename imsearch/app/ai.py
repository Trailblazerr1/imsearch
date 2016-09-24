from clarifai.client import ClarifaiApi
from shutil import copy
import json
import operator
import os
import sys

def imtags(tag_histogram):
    image_tag_lists = []
    clarifai_api = ClarifaiApi()

    orig_photo_dir = 'pic'
    if orig_photo_dir[len(orig_photo_dir) - 1] != '/':
        orig_photo_dir += '/'

    image_paths = os.listdir(orig_photo_dir)
    tagdict = {}
    for path in range(0, len(image_paths)):
        result = clarifai_api.tag_images(open('pic' +'/'+ image_paths[path], 'rb'))['results'][0]['result']['tag']['classes']
        image_tag_lists.append(result)
        print('Processing...')
        tagdict[image_paths[path]] = result
        for tag in result:
            if (tag in tag_histogram):
                tag_histogram[tag] += 1
            else:
                tag_histogram[tag] = 1
    return tagdict