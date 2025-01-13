from django.db import models
from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator

class Wilaya(models.Model):
    code = models.CharField(max_length=50, unique=True, validators=[MinLengthValidator(2)])
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Moughataa(models.Model):
    code = models.CharField(max_length=50, unique=True, validators=[MinLengthValidator(2)])
    label = models.CharField(max_length=200)
    wilaya = models.ForeignKey(Wilaya, on_delete=models.PROTECT, related_name='moughataa_set')

    def __str__(self):
        return self.label

class Commune(models.Model):
    code = models.CharField(max_length=50, unique=True, validators=[MinLengthValidator(2)])
    name = models.CharField(max_length=200)
    moughataa = models.ForeignKey(Moughataa, on_delete=models.PROTECT, related_name='commune_set')

    def __str__(self):
        return self.name

class ProductType(models.Model):
    code = models.CharField(max_length=50, unique=True, validators=[MinLengthValidator(2)])
    label = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.label

class Product(models.Model):
    code = models.CharField(max_length=50, unique=True, validators=[MinLengthValidator(2)])
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    unit_measure = models.CharField(max_length=50)
    product_type = models.ForeignKey(ProductType, on_delete=models.PROTECT, related_name='products')

    def __str__(self):
        return self.name

class PointOfSale(models.Model):
    SALE_TYPES = [
        ('supermarket', 'Supermarché'),
        ('market', 'Marché'),
        ('shop', 'Boutique'),
        ('other', 'Autre')
    ]

    code = models.CharField(max_length=50, unique=True, validators=[MinLengthValidator(2)])
    type = models.CharField(max_length=20, choices=SALE_TYPES)
    gps_lat = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    gps_lon = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    commune = models.ForeignKey(Commune, on_delete=models.PROTECT, related_name='points_of_sale')

    def __str__(self):
        return f"{self.code} - {self.get_type_display()}"

class ProductPrice(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='prices')
    point_of_sale = models.ForeignKey(PointOfSale, on_delete=models.PROTECT, related_name='product_prices')
    value = models.DecimalField(max_digits=10, decimal_places=2)
    date_from = models.DateField()
    date_to = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.product.name} - {self.value} ({self.date_from})"

class Cart(models.Model):
    code = models.CharField(max_length=50, unique=True, validators=[MinLengthValidator(2)])
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class CartProduct(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.PROTECT, related_name='cart_products')
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='cart_products')
    weighting = models.DecimalField(
        max_digits=5, 
        decimal_places=2, 
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        help_text="Pondération du produit dans le panier (en %)"
    )
    date_from = models.DateField()
    date_to = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.product.name} in {self.cart.name}"