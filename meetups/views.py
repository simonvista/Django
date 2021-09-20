from django.shortcuts import render
from django.http import HttpResponse
from .models import Meetup

# Create your views here.
def index(req):
    # return HttpResponse("Hello World")
    # fetch all meetups from DB
    meetups=Meetup.objects.all()

    return render(req,'meetups/index.html',{
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