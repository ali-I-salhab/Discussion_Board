from django.contrib import admin

from boards.models import Board
from .models import Board, Post, Topic
# Register your models here.
admin.site.register(Board)
admin.site.register(Topic)
admin.site.register(Post)