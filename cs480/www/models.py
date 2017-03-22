from django.db import models

# Create your models here.
class projects(models.Model):
	title = models.CharField(max_length =50)
	name   = models.CharField(max_length =50)
	image  = models.CharField(max_length = 200)
	year  = models.CharField(max_length = 50)

	def __str__(self):
		return self.name
