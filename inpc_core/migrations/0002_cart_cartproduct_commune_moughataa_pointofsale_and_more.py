# Generated by Django 4.2.9 on 2025-01-13 10:37

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inpc_core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=50, unique=True, validators=[django.core.validators.MinLengthValidator(2)])),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CartProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weighting', models.DecimalField(decimal_places=2, help_text='Pondération du produit dans le panier (en %)', max_digits=5, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('date_from', models.DateField()),
                ('date_to', models.DateField(blank=True, null=True)),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='cart_products', to='inpc_core.cart')),
            ],
        ),
        migrations.CreateModel(
            name='Commune',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=50, unique=True, validators=[django.core.validators.MinLengthValidator(2)])),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Moughataa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=50, unique=True, validators=[django.core.validators.MinLengthValidator(2)])),
                ('label', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='PointOfSale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=50, unique=True, validators=[django.core.validators.MinLengthValidator(2)])),
                ('type', models.CharField(choices=[('supermarket', 'Supermarché'), ('market', 'Marché'), ('shop', 'Boutique'), ('other', 'Autre')], max_length=20)),
                ('gps_lat', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True)),
                ('gps_lon', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True)),
                ('commune', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='points_of_sale', to='inpc_core.commune')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=50, unique=True, validators=[django.core.validators.MinLengthValidator(2)])),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, null=True)),
                ('unit_measure', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ProductPrice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date_from', models.DateField()),
                ('date_to', models.DateField(blank=True, null=True)),
                ('point_of_sale', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='product_prices', to='inpc_core.pointofsale')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='prices', to='inpc_core.product')),
            ],
        ),
        migrations.CreateModel(
            name='ProductType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=50, unique=True, validators=[django.core.validators.MinLengthValidator(2)])),
                ('label', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Wilaya',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=50, unique=True, validators=[django.core.validators.MinLengthValidator(2)])),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.RemoveField(
            model_name='pointsdeventes',
            name='region',
        ),
        migrations.AlterUniqueTogether(
            name='prix',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='prix',
            name='points_de_vente',
        ),
        migrations.RemoveField(
            model_name='prix',
            name='produit',
        ),
        migrations.RemoveField(
            model_name='produits',
            name='groupe_produit',
        ),
        migrations.DeleteModel(
            name='GroupsProduits',
        ),
        migrations.DeleteModel(
            name='PointsDeVentes',
        ),
        migrations.DeleteModel(
            name='Prix',
        ),
        migrations.DeleteModel(
            name='Produits',
        ),
        migrations.DeleteModel(
            name='Regions',
        ),
        migrations.AddField(
            model_name='product',
            name='product_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='products', to='inpc_core.producttype'),
        ),
        migrations.AddField(
            model_name='moughataa',
            name='wilaya',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='moughataa_set', to='inpc_core.wilaya'),
        ),
        migrations.AddField(
            model_name='commune',
            name='moughataa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='commune_set', to='inpc_core.moughataa'),
        ),
        migrations.AddField(
            model_name='cartproduct',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='cart_products', to='inpc_core.product'),
        ),
    ]