from django.contrib import admin
from django.contrib.auth.models import Group, User
from django.contrib.auth.admin import UserAdmin
from .models import Profile

class ProfileInline(admin.StackedInline):
    model = Profile
    verbose_name = 'شهر'

class ExtendUserAdmin(UserAdmin):
    inlines = (ProfileInline, )
    list_display = ('username', 'email', 'get_profile', 'is_staff', 'is_active')
    list_editable = ('is_active', 'is_staff')
    search_fields = ('username',)
    fieldsets = (
        ('اطلاعات', {'fields': ('username', 'first_name', 'last_name', 'email', 'password')}),
        ('دسترسی', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
    )
    def get_profile(self, obj):
        return obj.profile

    get_profile.short_description = 'شهر'

admin.site.unregister(Group)
admin.site.unregister(User)
admin.site.register(User, ExtendUserAdmin)