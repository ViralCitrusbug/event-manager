from django.db import models
# Create your models here.


class EventDate(models.Model):
    date = models.DateField()

    def __str__(self) -> str:
        return str(self.date)

class Event(models.Model):
    date = models.ForeignKey(EventDate,on_delete=models.CASCADE)
    name = models.CharField(max_length=200,null=False)
    organizer = models.CharField(max_length=50,null=False)
    email = models.EmailField()
    post_code = models.IntegerField()
    phone_number = models.IntegerField()


    def __str__(self) -> str:
        return self.name

class EventTime(models.Model):
    event = models.ForeignKey(Event,on_delete=models.CASCADE)
    time = models.TimeField(unique=True)

    def __str__(self) -> str:
        return str(self.time)