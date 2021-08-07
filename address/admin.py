from django.contrib import admin

# Register your models here.
from address.models import Country, Province, City, County, Address


# ,,,,
@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ['name', 'created']


@admin.register(Province)
class ProvinceAdmin(admin.ModelAdmin):
    list_display = ['name', 'country', 'created']


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ['name', 'province', 'created']


@admin.register(County)
class CountyAdmin(admin.ModelAdmin):
    list_display = ['name', 'city', 'created']


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ['customer', 'country', 'province', 'city', 'county', 'address', 'company', 'email', 'created']
