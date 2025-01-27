# Generated by Django 5.0.1 on 2025-01-12 17:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GroupsProduits',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_group', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Regions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_region', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Produits',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_produit', models.CharField(max_length=100)),
                ('ponderation', models.FloatField()),
                ('groupe_produit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inpc_core.groupsproduits')),
            ],
        ),
        migrations.CreateModel(
            name='PointsDeVentes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_point', models.CharField(max_length=100)),
                ('longitude', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True)),
                ('latitude', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True)),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inpc_core.regions')),
            ],
        ),
        migrations.CreateModel(
            name='Prix',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prix', models.DecimalField(decimal_places=2, max_digits=10)),
                ('annee', models.IntegerField()),
                ('mois', models.IntegerField()),
                ('points_de_vente', models.ManyToManyField(to='inpc_core.pointsdeventes')),
                ('produit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inpc_core.produits')),
            ],
            options={
                'unique_together': {('produit', 'annee', 'mois')},
            },
        ),
    ]
