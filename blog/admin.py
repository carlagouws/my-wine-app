from django.contrib import admin
from blog.models import Wine

class WineAdmin(admin.ModelAdmin):
    model = Wine
    list_display = ('name', 'type', 'variety', 'vintage', 'region', 'comments',)

admin.site.register(Wine, WineAdmin)
