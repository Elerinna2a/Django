from django.db import models


class Utilisateur(models.Model):
    nom = models.CharField(max_length=30)
    age = models.IntegerField()
    is_admin = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.nom}"