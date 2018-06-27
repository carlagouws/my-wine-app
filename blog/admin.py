from django.contrib import admin
from blog.models import Wine

class WineAdmin(admin.ModelAdmin):
    model = Wine
    list_display = ('name', 'created_date', 'image', 'image_2', 'rating', 'type', 'variety', 'vintage', 'region', 'shop', 'price', 'comments',)

admin.site.register(Wine, WineAdmin)
