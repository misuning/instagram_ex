from django.db import models


class Comment(models.Model):
	name = models.CharField(max_length = 50)
	content = models.CharField(max_length = 500)
	created_at = models.DateTimeField(auto_now_add=True)
	

	class Meta:
		db_table = "comments"


