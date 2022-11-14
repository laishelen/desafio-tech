from django.db import models

class usuarios(models.Model):
    login = models.CharField(max_length=50, null=False, blank=False)
    password = models.CharField(max_length=20, null=True, blank=True)
    dataNascimento = models.DateField(null=False, blank=False)

  


