from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin
from .models import User
# Register your models here.
UserAdmin.list_display = ('email', 'first_name',
                          'last_name', 'is_active', 'date_joined', 'is_staff','creator_id')

admin.site.register(User, UserAdmin)
