from django.http import HttpResponse
from django.shortcuts import render

from collections import defaultdict
import operator


def homepage(request):
    return render(request, 'home.html')

def count(request):
    fulltext = request.GET['fulltext']
    word_list = fulltext.split()
    word_count = len(word_list)

    word_dict = defaultdict(int)

    for word in word_list:
         word_dict[word] += 1

    sorted_words = sorted(word_dict.items(), key=operator.itemgetter(1), reverse=True)
    return render(request, 'count.html', {'fulltext':fulltext, 'word_count':word_count, 'sorted_words':sorted_words})

def about(request):
    return render(request, "about.html")
