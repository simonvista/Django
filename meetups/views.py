from meetups.forms import RegistrationForm
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
    try:
        selected_meetup=Meetup.objects.get(slug=meetup_slug)
        if req.method=='GET':
            registration_form=RegistrationForm()            
        else:
            registration_form=RegistrationForm(req.POST)
            if registration_form.is_valid():
                participant=registration_form.save()    # save form data to DB
                selected_meetup.participants.add(participant)
        return render(req,'meetups/meetup-details.html',{
                'meetup_found':True,
                'meetup':selected_meetup,
                'form':registration_form
            })
    except Exception as exc:
        return render(req,'meetups/meetup-details.html',{
            'meetup_found':False
        })
    