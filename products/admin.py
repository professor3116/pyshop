from django.contrib import admin
from .models import Product
from .models import Offers

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', )


class OffersAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount',  'description')


admin.site.register(Product, ProductAdmin)
admin.site.register(Offers, OffersAdmin)


