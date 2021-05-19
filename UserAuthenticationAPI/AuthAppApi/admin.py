from django.contrib import admin
from AuthAppApi.models import Users


class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'email', 'username', 'phone', 'password']

admin.site.register(Users, UserAdmin)
