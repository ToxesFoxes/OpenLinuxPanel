from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class SystemStat(models.Model):
	# ['cpu', 'memory','disk']
	# store only order for user
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=50)
	order = models.IntegerField()
	active = models.BooleanField(default=True)

	user = models.ForeignKey(User, on_delete = models.CASCADE, blank = True, null = True)

	def __str__(self):
		return self.name