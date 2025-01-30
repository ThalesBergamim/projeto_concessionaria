from django.contrib import admin
from ecom.models import Car, Brand

class CarAdmin(admin.ModelAdmin):
    list_display = ('model', 'brand', 'price', 'year_fabrication', 'year_model', 'plate',)
    search_fields = ('name', 'brand',)
    
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    
    
admin.site.register(Car, CarAdmin)
admin.site.register(Brand, BrandAdmin)

