from django.contrib import admin
from . models import MovieInfo, Production, CensorInfo, Actor
# Register your models here.
admin.site.register(MovieInfo)
admin.site.register(Production)
admin.site.register(CensorInfo)
admin.site.register(Actor)