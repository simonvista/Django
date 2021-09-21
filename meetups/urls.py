from django.urls.conf import path
from . import views

urlpatterns = [
    path('meetups/',views.index,name='all-meetups'), #domain.com/meetups
    # path('meetups/success',views.confirm_registration,name='confirm-registration'),
    path('meetups/<slug:meetup_slug>/success',views.confirm_registration,name='confirm-registration'),
    path('meetups/<slug:meetup_slug>',views.meetup_details,name='meetup-details'), #domain.com/1st-meetup
]