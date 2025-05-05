from django.db import models

class userContact(models.Model):
    FullName = models.CharField(max_length=100)
    Email = models.EmailField()
    PhoneNo = models.CharField(max_length=15)
    Address = models.TextField()
    Date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.FullName
class time(models.Model):
    Date = models.DateTimeField(auto_now_add=True)
    
    