from django.contrib import admin
from cars.models import Car, Brand



class Brand_Admin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class Car_Admin(admin.ModelAdmin):
    list_display = ('model','brand','factory_year', 'model_year', 'value')
    search_fields = ('model','brand',)


admin.site.register(Car, Car_Admin)
admin.site.register(Brand, Brand_Admin)

