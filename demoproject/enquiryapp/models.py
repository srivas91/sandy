from django.db import models

# Create your models here.
class Enquiry(models.Model):
     id=models.IntegerField(primary_key=True)
     name=models.CharField(max_length=30)
     course=models.CharField(max_length=20)

     def __str__(self):
         return f'{self.id}-{self.name}-{self.course}'