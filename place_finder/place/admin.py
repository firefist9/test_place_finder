from django.contrib import admin
from .models import Company, Category

#admin.site.register(Company)
#admin.site.register(Category)

class CompanayInline(admin.StackedInline):
    model = Company
    extra = 3

class CategoryInline(admin.ModelAdmin):
    inlines = [
        CompanayInline,
    ]

admin.site.register(Category, CategoryInline)
admin.site.register(Company)
