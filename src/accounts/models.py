from django.db import models
import re 
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse
from datetime import date

User = get_user_model()

# Create your models here.

def phone_validator(value):
	reg = re.compile(r'^\d\d\d\d\d\d\d\d\d\d$')
	number = reg.match(value)
	if number is None:
		raise ValidationError("The number is not valid")
	return value 


class Profile(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE)
	CHOICES = (('male','male'),('female','female'))
	MARITAL = (('Married','Married'),('Single','Single'),('Divorced','Divorced'))
	phone_no = models.CharField(max_length=15,unique=True,validators=[phone_validator])
	birth_date = models.DateField()
	bio = models.TextField(max_length=200,null=True,blank=True)
	gender = models.CharField(max_length=10,choices=CHOICES,null=True)
	marital_status = models.CharField(max_length=10,choices=MARITAL,null=True)
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
	latitude = models.CharField(max_length=100,null=True)
	longitude = models.CharField(max_length=100,null=True)
	RELIGION = (('Hinduism','Hinduism'),('Christian','Christian'),('Buddhism','Buddhism'),('Muslim','Muslim'),('Sikh','Sikh'),('Jain','Jain'))
	religion = models.CharField(max_length=20,null=True,blank=True,choices=RELIGION)
	QUALIFICATION = (('Under Graduate','Under Graduate'),('Graduate','Graduate'),('Post Graduate','Post Graduate'))
	qualification = models.CharField(max_length=30,null=True,choices=QUALIFICATION)
	height = models.IntegerField(null=True,blank=True)

	def __unicode__(self):
		return "%s's profile" % self.user

	def __str__(self):
		return "%s's profile" % self.user

	def get_absolute_url(self):
		return reverse('detail', kwargs={'pk':self.pk})

	def get_age(self):
		today = date.today()
		age = today.year - self.birth_date.year
		age = int(age)
		return age







