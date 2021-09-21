from django.contrib import admin
from .models import Meetup,Location

# Register your models here.
# admin.site.register(Meetup)
class MeetupAdmin(admin.ModelAdmin):
    list_display=('title','slug')
    # list_filter=('title',)
    list_filter=('location',)
    prepopulated_fields={'slug':('title',)}

admin.site.register(Meetup,MeetupAdmin)
admin.site.register(Location)