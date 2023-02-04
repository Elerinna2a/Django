from django.db import models


class Client(models.Model):
    nom = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self) -> str:
        return f"{self.nom}"
    

class Entreprise(models.Model):
    nom = models.CharField(max_length=30)
    domaine = models.CharField(max_length=30)

    clients = models.ManyToManyField('Client', related_name="entreprises")

    def __str__(self) -> str:
        return f"{self.nom}"
    

class Reclamation(models.Model):
    description = models.CharField(max_length=30)

    client = models.ForeignKey('Client', related_name="reclamations", null=True, blank=True, on_delete=models.CASCADE)
    entreprise = models.ForeignKey('Entreprise', related_name="reclamations", null=True, blank=True, on_delete=models.CASCADE)

    traite = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.id}" # type: ignore