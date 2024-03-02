from django.contrib import admin
from .models import Product, Access, Lesson, ProductGroups

admin.site.register(Product)
admin.site.register(Access)
admin.site.register(Lesson)
admin.site.register(ProductGroups)
