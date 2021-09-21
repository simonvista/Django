from meetups.forms import RegistrationForm
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Meetup,Participant

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
                # participant=registration_form.save()    # save form data to DB -> participant email can be used only once
                user_email=registration_form.cleaned_data['email']
                participant,_=Participant.objects.get_or_create(email=user_email)
                selected_meetup.participants.add(participant)
                return redirect('confirm-registration')
        return render(req,'meetups/meetup-details.html',{
                'meetup_found':True,
                'meetup':selected_meetup,
                'form':registration_form
            })
    except Exception as exc:
        return render(req,'meetups/meetup-details.html',{
            'meetup_found':False
        })

def confirm_registration(req):
    return render(req,'meetups/registration-success.html')