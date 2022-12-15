from django.contrib import admin
from .models import Post
from .citymodels import City

admin.site.register(Post)
admin.site.register(City)