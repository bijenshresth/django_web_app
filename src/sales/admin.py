from django.contrib import admin
from django.contrib.admin.options import csrf_protect_m
from .models import Position, Sale, CSV
# Register your models here.


admin.site.register(Position)
admin.site.register(Sale)
admin.site.register(CSV)

