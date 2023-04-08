# Generated by Django 4.0.6 on 2022-08-05 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pred', '0002_burreau'),
    ]

    operations = [
        migrations.CreateModel(
            name='pc_gamer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=200)),
                ('prix', models.CharField(max_length=10)),
                ('taille_ecran', models.CharField(max_length=10)),
                ('type_ecran', models.CharField(max_length=10)),
                ('type_processeur', models.CharField(max_length=30)),
                ('reference_processeur', models.CharField(max_length=100)),
                ('ram', models.CharField(max_length=3)),
                ('rom', models.CharField(max_length=15)),
                ('carte_graphique', models.CharField(max_length=50)),
                ('reference_carte_graphique', models.CharField(max_length=30)),
                ('systeme_exploitation', models.CharField(max_length=30)),
                ('garanti', models.CharField(max_length=2)),
                ('store', models.CharField(max_length=20)),
                ('link', models.CharField(max_length=500)),
                ('reference', models.CharField(max_length=100)),
            ],
        ),
    ]
