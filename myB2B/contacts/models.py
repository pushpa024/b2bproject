from django.db import models


class BasicContact(models.Model):
    name = models.CharField(max_length=150, null=True, blank=True, default="")
    email = models.EmailField(max_length=150)
    phone = models.CharField(max_length=15, null=True, blank=True)
    country = models.CharField(max_length=30, null=True, blank=True)
    message = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    modified_on = models.DateTimeField(auto_now=True, null=True, blank=True)