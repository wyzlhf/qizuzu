from django.contrib import admin

# Register your models here.
from lease.models import Category, Scenario, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','created_date','updated_date']


@admin.register(Scenario)
class ScenarioAdmin(admin.ModelAdmin):
    list_display = ['name', 'category','created_date','updated_date']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['short_name', 'scenario', 'rent_price_not_null', 'rent_price_second',
                    'rent_price_third', 'deposit','created_date','updated_date']
