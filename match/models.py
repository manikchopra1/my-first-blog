from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

class Propose(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='to_user')
    message = models.TextField(max_length=200)
    sent_at = models.DateTimeField(default=timezone.now)
    relationshipstatus = models.CharField(max_length=50, choices= [('single', 'Single'), ('committed', 'Committed'),], default='single')

