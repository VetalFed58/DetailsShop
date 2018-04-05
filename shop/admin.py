from django.contrib import admin
from .models import Detail, DetailImage

class DetailImageInline(admin.TabularInline):
    model = DetailImage
    extra = 3

class DetailAdmin(admin.ModelAdmin):
    inlines = [ DetailImageInline, ]

admin.site.register(DetailImage)
admin.site.register(Detail)

