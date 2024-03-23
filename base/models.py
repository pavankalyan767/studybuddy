from django.db import models
from django.contrib.auth.models import User
# Create your models here.
# there will be multiple rooms 
# there will be different topics like physics computer science web dev
# and there will be messages in all the rooms and message requires metadata like when it is created and updated
class Room(models.Model):
    host = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    topic = models.ForeignKey('Topic',on_delete=models.SET_NULL,null=True)
    name = models.CharField(max_length=255)
    # since User is already referenced i should use relatedname
    participants = models.ManyToManyField(User,related_name='participants',blank=True)
    description = models.CharField(max_length=10000)
    created = models.DateTimeField(auto_now=True) #records when the room was created
    updated = models.DateTimeField(auto_now_add=True)# records everytime save is done

    class Meta:
        ordering = ['-created','-updated'] # - indicated descending order 
        # so i can just use ordering in meta class and update based 
        # on different columns just like i do it in sql 


    def __str__(self):
        return self.name
    
class Message(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    room = models.ForeignKey(Room,on_delete=models.CASCADE) #here one to many
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.body[0:50]
    class Meta:
        ordering = ['-created','-updated']
    
class Topic(models.Model):
    name = models.TextField(set)
    def __str__(self):
        return self.name