import datetime

from django.db import models
from django.utils import timezone

class Suggestions(models.Model):
  suggestion = models.CharField(max_length=750)
  created_at = models.DateTimeField('Date created')
  def __str__(self) -> str:
    return str(self.suggestion)
  def was_created_recently(self) -> bool:
    return self.created_at >= timezone.now() - datetime.timedelta(days=1)