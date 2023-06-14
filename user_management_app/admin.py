from django.contrib import admin
from .models import Profile

# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    list_display = ["id", "get_username", "location", "designation"]

    def get_username(self, obj):
        return obj.user.username

    get_username.short_description = 'username'


admin.site.register(Profile, ProfileAdmin)