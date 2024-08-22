from django.db import models


class Timestamp(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
