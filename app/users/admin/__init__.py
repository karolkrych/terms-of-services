from django.contrib import admin
from .user_admin import UserAdmin
from users.models import User

admin.site.register(User, UserAdmin)
