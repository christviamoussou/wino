
from django.db import models

class UserInfo(models.Model):
    ip = models.CharField(max_length=100)
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    poste = models.CharField(max_length=100)
    cc = models.EmailField()

    def __str__(self):
        return f"{self.nom} {self.prenom}"

