from django.contrib import admin
from .models import Comment,UserProfile,Post,Tag,PostUserLikes

# Register your models here.
admin.site.register([Comment,UserProfile,Post,Tag,PostUserLikes])