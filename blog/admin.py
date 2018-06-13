from django.contrib import admin
from blog.models import Wine

class WineAdmin(admin.ModelAdmin):
    model = Wine
    list_display = ('name', 'vintage', 'comments')
    prepopulated_fields = {'slug': ('name', )}

admin.site.register(Wine, WineAdmin)
