from django.db import models

class players(models.Model):
	
	name = models.CharField(max_length=50)
	email = models.EmailField()
	team_name = models.CharField(max_length=50)
	sports = models.CharField(max_length=50)
	college_name = models.CharField(max_length=50)
	city = models.CharField(max_length=20)
	state = models.CharField(max_length=50)
	phone_no = models.CharField(max_length=15)

	class Meta:
		db_table = "Players_Detail"


