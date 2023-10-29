from django.contrib import admin

# Register your models here.
from .models import profile,upload
admin.site.register(profile)
admin.site.register(upload)