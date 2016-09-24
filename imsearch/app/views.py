from django.shortcuts import render, HttpResponse
from app.ai import *
import os.path
import json
import os
import operator

# Create your views here

def index(request):
    return render(request, 'app/index.html')





def pick(request):
    tag_histogram = {}
    PATH='hi.txt'
    if os.path.isfile(PATH) and os.access(PATH, os.R_OK):
        #data = json.load(open("di.txt"))
        top_five_tags = json.load(open("hi.txt"))

    else:
        data = imtags(tag_histogram)
        #top 10 tags
        tag_tuples = sorted(tag_histogram.items(), key=operator.itemgetter(1))
        top_five_tuples = tag_tuples[len(tag_tuples) - 10:len(tag_tuples)]
        top_five_tags = []
        for i in top_five_tuples:
            print(i[0])
            top_five_tags.append(i[0])
        json.dump(data,open("di.txt",'w'))
        json.dump(top_five_tags,open("hi.txt",'w'))

    return render(request, 'app/pick.html', {'tag':top_five_tags})







def search(request):
	#tag = {'amusement_0491.jpg': ['field', 'outdoors', 'one'], 'amusement_0489.jpg': ['people', 'street', 'road'], 'amusement_0492.jpg': ['nature', 'leaf', 'summer', 'beautiful']}
    if request.method == 'POST':
        sterm = request.POST.get('term')
    PATH='di.txt'
   
    #data = {'amusement_0493.jpg': ['tree', 'landscape', 'nature', 'panoramic', 'sky', 'grass', 'hayfield', 'cloud', 'outdoors', 'field', 'rural', 'no person', 'fair weather', 'horizon', 'wood', 'season', 'idyllic', 'sun', 'summer', 'countryside'], 'amusement_0489.jpg': ['people', 'street', 'city', 'business', 'transportation system', 'adult', 'stock', 'balloon', 'one', 'urban', 'shopping', 'travel', 'modern', 'market', 'commerce', 'vehicle', 'man', 'portrait', 'industry', 'road'], 'amusement_0490.jpg': ['woman', 'one', 'girl', 'adult', 'nature', 'people', 'portrait', 'outdoors', 'fashion', 'wear', 'blond', 'model', 'beautiful', 'young', 'lifestyle', 'dress', 'summer', 'fall', 'recreation', 'freedom'], 'amusement_0492.jpg': ['nature', 'flora', 'flower', 'leaf', 'summer', 'no person', 'garden', 'growth', 'close-up', 'floral', 'outdoors', 'blur', 'bright', 'color', 'petal', 'grass', 'season', 'blooming', 'delicate', 'beautiful'], 'amusement_0488.jpg': ['portrait', 'outdoors', 'people', 'adult', 'one', 'man', 'daylight', 'side view', 'woman', 'music', 'profile', 'festival', 'wear', 'park', 'musician', 'nature', 'leisure', 'fashion', 'love', 'relaxation'], 'amusement_0491.jpg': ['field', 'outdoors', 'poppy', 'summer', 'flower', 'hayfield', 'nature', 'leisure', 'sky', 'fun', 'happiness', 'enjoyment', 'grass', 'joy', 'girl', 'adult', 'people', 'freedom', 'woman', 'one'], 'amusement_0487.jpg': ['sea', 'beach', 'sand', 'outdoors', 'water', 'relaxation', 'fun', 'summer', 'freedom', 'sky', 'seashore', 'carefree', 'nature', 'fair weather', 'enjoyment', 'travel', 'leisure', 'motion', 'surf', 'balance']}
    tag_histogram = {}
    orig_photo_dir = 'pic'
    image_paths = os.listdir(orig_photo_dir)
    if os.path.isfile(PATH) and os.access(PATH, os.R_OK):
        data = json.load(open("di.txt"))
        if len(data.keys()) != len(image_paths):
            data = imtags(tag_histogram)
            json.dump(data,open("di.txt",'w'))
            tag_tuples = sorted(tag_histogram.items(), key=operator.itemgetter(1))
            top_five_tuples = tag_tuples[len(tag_tuples) - 10:len(tag_tuples)]
            top_five_tags = []
            for i in top_five_tuples:
                print(i[0])
                top_five_tags.append(i[0])        
            json.dump(top_five_tags,open("hi.txt",'w'))
    else:
        data = imtags(tag_histogram)
        json.dump(data,open("di.txt",'w'))
        tag_tuples = sorted(tag_histogram.items(), key=operator.itemgetter(1))
        top_five_tuples = tag_tuples[len(tag_tuples) - 10:len(tag_tuples)]
        top_five_tags = []
        for i in top_five_tuples:
            print(i[0])
            top_five_tags.append(i[0])
        json.dump(top_five_tags,open("hi.txt",'w'))

        #json.dump(data,open("di.txt",'w'))
    return render(request, 'app/search.html', {'inp': sterm , 'data' : data})
    




def viewname(request, uid):

    PATH='di.txt'
    tag_histogram = {}
    if os.path.isfile(PATH) and os.access(PATH, os.R_OK):
        data = json.load(open("di.txt"))    
        tag_histogram = json.load(open("hi.txt"))

    else:
        data = imtags(tag_histogram)
        json.dump(data,open("di.txt",'w'))

        json.dump(tag_histogram,open("hi.txt",'w'))

        #json.dump(data,open("di.txt",'w'))
    return render(request, 'app/search.html', {'inp': uid , 'data' : data , 'his':tag_histogram})
