from django.db import models

class GroupsProduits(models.Model):
    nom_group = models.CharField(max_length=100)

    def __str__(self):
        return self.nom_group

class Regions(models.Model):
    nom_region = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nom_region

class PointsDeVentes(models.Model):
    nom_point = models.CharField(max_length=100)
    region = models.ForeignKey(Regions, on_delete=models.CASCADE)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)

    def __str__(self):
        return f"{self.nom_point} - {self.region}"

class Produits(models.Model):
    nom_produit = models.CharField(max_length=100)
    groupe_produit = models.ForeignKey(GroupsProduits, on_delete=models.CASCADE)
    ponderation = models.FloatField()

    def __str__(self):
        return self.nom_produit

class Prix(models.Model):
    produit = models.ForeignKey(Produits, on_delete=models.CASCADE)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    annee = models.IntegerField()
    mois = models.IntegerField()
    points_de_vente = models.ManyToManyField(PointsDeVentes)

    class Meta:
        unique_together = ['produit', 'annee', 'mois']

    def __str__(self):
        return f"{self.produit} - {self.annee}-{self.mois}"