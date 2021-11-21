from django.db import models
# Create your models here.


class Psycology(models.Model):
    textinput = models.TextField()
    textoutput = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']


