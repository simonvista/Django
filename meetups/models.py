from django.db import models

# Create your models here ->Meetups table
class Location(models.Model):
    name=models.CharField(max_length=200)
    address=models.CharField(max_length=300)

    def __str__(self) -> str:
        return f'{self.name} - {self.address}'

class Participant(models.Model):
    email=models.EmailField(unique=True)

    def __str__(self):
        return f'{self.email}'    

class Meetup(models.Model):
    title=models.CharField(max_length=200)
    slug=models.SlugField(unique=True)
    description=models.TextField()
    image=models.ImageField(upload_to="images")
    # one-to-many
    location=models.ForeignKey(Location,on_delete=models.CASCADE)
    # many-to-many. blank=True -> form field can be empty. null=True -> DB field can be empty
    participants=models.ManyToManyField(Participant, blank=True,null=True)

    def __str__(self):
        return f'{self.title} - {self.slug}'

# one-to-many -> one location has many meetups. one meetup has only one location
# many-to-many -> participant <-> meetup