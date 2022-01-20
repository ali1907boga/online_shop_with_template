from django.contrib import admin
from .models import *



class ImageProductInline(admin.TabularInline):
    model = Image_pro
    extra = 2

class VarientAdminInline(admin.TabularInline):
    model = Variant
    extra = 3

class ProductAdmin(admin.ModelAdmin):


    inlines = [VarientAdminInline,ImageProductInline]


admin.site.register(Category)
admin.site.register(Product,ProductAdmin)
admin.site.register(Variant)
admin.site.register(Size)
admin.site.register(Color)
admin.site.register(Comment)
admin.site.register(Image_pro)
