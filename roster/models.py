from django.db import models

# Create your models here.

class Student(models.Model):
	name = models.CharField(max_length=50)
	number = models.CharField(unique=True, max_length=2)
	position = models.CharField(null=True, max_length=25)
	url = models.TextField(null=True, max_length =100)
	height = models.CharField(null=True, max_length=5)
	year = models.CharField(null=True, max_length=5)
	hometown = models.CharField(null=True, max_length=25)
	major = models.CharField(null=True, max_length=50)
	stats = models.TextField(null=True, max_length=5000)
	bio = models.TextField(null=True, max_length=5000)
	national = models.TextField(null=True, max_length=5000)
	before = models.TextField(null=True, max_length=5000)

	class Meta(object):
		ordering = ('number', 'name')

	def __unicode__(self):
		return U'%s %s' %(self.name, self.number)
