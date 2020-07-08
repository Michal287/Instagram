from django.contrib import admin
from .models import UserProfile, Post, FavoritesPosts

admin.site.register(UserProfile)
admin.site.register(Post)
admin.site.register(FavoritesPosts)

