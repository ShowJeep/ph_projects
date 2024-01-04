from django.shortcuts import render
import datetime

# Create your views here.
def home(request):
    d={
        'lst': ['Hello', 'world'],
        'time': datetime.datetime.now(),
        'val': 5,
        'num': [4,5,6],
        'nm': 
        [
            {'name': 'Josh', 'age': 19},
            {'name': 'Dave', 'age': 22},
            {'name': 'Joe', 'age': 31},
        ],
        'str':"I Am doing pratice Now.",
        'data': 
        [
            {
                'id': '377386', 
                'name': 'Grace Davis', 
                'courses': []
            }
        ]  
    }
    return render(request, 'home.html',d)