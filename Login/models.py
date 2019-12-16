from django.db import models

# Create your models here.
class login(models.Model):
	username=models.CharField(max_length=50,unique=True)
	password=models.CharField(max_length=50)


	def __str__(self):

		return self.username