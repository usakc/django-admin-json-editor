from django.db import models
from django.contrib.postgres.fields import JSONField

class JSONModel(models.Model):
	data = JSONField(default={
		'text': 'some text',
		'status': False,
		})