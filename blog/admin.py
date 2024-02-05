from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
from .models import Blog, Comment, Author

admin.site.register(User, UserAdmin)
admin.site.register(Blog)
admin.site.register(Comment)
admin.site.register(Author)
