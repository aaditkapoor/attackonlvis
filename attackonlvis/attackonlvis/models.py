from django.db import models



class PasswordCollector(models.Model):
	password = models.CharField(max_length=500)

	def __unicode__(self):
		return self.password

