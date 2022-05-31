
from django.contrib import admin
from categories.models import Category


class CategoryAdmin(admin.ModelAdmin):
    field = ['name', ]


admin.site.register(Category, CategoryAdmin)
