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

def meetup_details(req,meetup_slug):
    print(meetup_slug)
    selected_meetup={
            'title':'1st meetup',
            'description':'1st meetup'
        }
    return render(req,'meetups/meetup-details.html',{
        'meetup_title':selected_meetup['title'],
        'meetup_description':selected_meetup['description']
    })