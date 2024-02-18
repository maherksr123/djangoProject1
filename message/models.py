from django.db import models
class query(models.Model):
    name=models.CharField(max_length=20)
    fathername=models.CharField(max_length=20)
    email = models.EmailField()
    contact = models.CharField(max_length=20)
    subject=models.TextField(max_length=70)
    message=models.TextField(max_length=30)

    # def __str__(self):
    #     return self.name
# Create your models here.
