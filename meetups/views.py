from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(req):
    # return HttpResponse("Hello World")
    meetups=[
        {
            'title':'1st meetup',
            'location':'New York',
            'slug':'1st-meetup'
        },
        {
            'title':'2nd meetup',
            'location':'Paris',
            'slug':'2nd-meetup'
        },
    ]
    return render(req,'meetups/index.html',{
        'show_meetups':True,
        'meetups':meetups
    })