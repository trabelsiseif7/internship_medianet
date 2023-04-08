from django.db import models


class product(models.Model) :
    nom = models.CharField( max_length = 200 )
    prix = models.CharField( max_length = 10 )
    taille_ecran = models.CharField( max_length = 10 )
    type_ecran = models.CharField( max_length = 10 )
    type_processeur = models.CharField( max_length = 30 )
    reference_processeur = models.CharField(max_length=100)
    ram = models.CharField( max_length = 3 )
    rom = models.CharField(max_length=15)
    carte_graphique = models.CharField( max_length = 50 )
    reference_carte_graphique = models.CharField( max_length = 30 )
    systeme_exploitation = models.CharField( max_length = 30 )
    garanti = models.CharField( max_length = 2 )
    store = models.CharField( max_length = 20 )
    link = models.CharField( max_length = 500 )
    reference = models.CharField(max_length=100)
    image_link = models.CharField( max_length = 500 )

class burreau(models.Model) :
    nom = models.CharField(max_length=200)
    prix = models.CharField(max_length=10)
    type_processeur = models.CharField(max_length=30)
    reference_processeur = models.CharField(max_length=100)
    ram = models.CharField(max_length=3)
    rom = models.CharField(max_length=15)
    carte_graphique = models.CharField(max_length=50)
    reference_carte_graphique = models.CharField(max_length=30)
    systeme_exploitation = models.CharField(max_length=30)
    garanti = models.CharField(max_length=2)
    store = models.CharField(max_length=20)
    link = models.CharField(max_length=500)
    reference = models.CharField(max_length=100)
    image_link = models.CharField(max_length=500)

class pc_gamer(models.Model) :
    nom = models.CharField( max_length = 200 )
    prix = models.CharField( max_length = 10 )
    taille_ecran = models.CharField( max_length = 10 )
    type_ecran = models.CharField( max_length = 10 )
    type_processeur = models.CharField( max_length = 30 )
    reference_processeur = models.CharField(max_length=100)
    ram = models.CharField( max_length = 3 )
    rom = models.CharField(max_length=15)
    carte_graphique = models.CharField( max_length = 50 )
    reference_carte_graphique = models.CharField( max_length = 30 )
    systeme_exploitation = models.CharField( max_length = 30 )
    garanti = models.CharField( max_length = 2 )
    store = models.CharField( max_length = 20 )
    link = models.CharField( max_length = 500 )
    reference = models.CharField(max_length=100)
    image_link = models.CharField( max_length = 500 )


class smartphone(models.Model):
    nom = models.CharField(max_length=200)
    prix = models.CharField(max_length=10)
    ram = models.CharField(max_length=100)
    rom = models.CharField(max_length=100)
    systeme_exploitation = models.CharField(max_length=100)
    ecran_size = models.CharField(max_length=100)
    camera = models.CharField(max_length=100)
    store = models.CharField(max_length=100)
    link = models.CharField(max_length=100)
    reference = models.CharField(max_length=100)
    image_link = models.CharField(max_length=500)

# Create your models here.

