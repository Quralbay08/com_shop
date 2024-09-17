from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe
# Register your models here.
admin.site.register(Category)
admin.site.register(Brend)

admin.site.register(Comments)

@admin.register(Product)
class Productclass(admin.ModelAdmin):
    list_display = ['name','brend','category','price','show_image']
    list_display_links = ['name','brend','category']
    list_filter = ['brend','category']
    list_editable = ['price']
    
    def show_image(self,photo):
        if photo.image1:
            return mark_safe(f"<img src='{photo.image1.url}' width=70>")
        return None
    show_image.__name__='Suwret'
