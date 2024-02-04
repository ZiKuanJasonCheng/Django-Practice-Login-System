from django.db import models

# Create your models here.
class Account(models.Model):
    username = models.CharField("username", max_length=20)
    password = models.CharField("password", max_length=30)
    datetime = models.DateTimeField("datetime")
    def __str__(self):
        return self.username
    
class Itinerary(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    it_name = models.CharField("it_name", max_length=20)

    def __str__(self):
        return self.it_name