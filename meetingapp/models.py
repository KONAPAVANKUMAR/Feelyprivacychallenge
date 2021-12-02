from django.db import models

# Create your models here.
class MeetingModel(models.Model):
    datetime = models.DateTimeField()
    manager = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    employee = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='employee',blank=True,null=True)
    