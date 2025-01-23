import django_filters
from .models import Product, ProductType

class ProductFilter(django_filters.FilterSet):
    product_type = django_filters.ModelChoiceFilter(
        queryset=ProductType.objects.all(),
        label="Type de Produit",
        field_name="product_type",
    )

    class Meta:
        model = Product
        fields = ['product_type']