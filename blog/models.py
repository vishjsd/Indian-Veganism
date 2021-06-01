from django.db import models

# Create your models here.
class Post(models.Model):
    sno= models.AutoField(primary_key=True)
    title= models.CharField(max_length=200)
    author= models.CharField(max_length=50)
    slug= models.CharField(max_length=150)
    timeStamp= models.DateTimeField(blank=True)
    content= models.TextField()
    image=models.ImageField(upload_to='pics')

    def __str__(self):
        return self.title +  " by " +  self.author
    