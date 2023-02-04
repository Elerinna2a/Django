from django.db import models


class Formation(models.Model):
    nom = models.CharField(max_length=30)

    def __str__(self) -> str:
        return f"{self.nom} !!"
