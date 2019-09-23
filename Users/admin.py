from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from .models import Profile, User, Organization, Permission
from django.contrib.auth.forms import UserCreationForm


# Register your models here.


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('organizationid',)


class MyUserAdmin(UserAdmin):
        add_form = CustomUserCreationForm
        fieldsets = UserAdmin.fieldsets + (
                (None, {'fields': ('organizationid',)}),
        )


class PermissionAdmin(admin.ModelAdmin):
    pass


class ProfileAdmin(admin.ModelAdmin):
    pass


class OrganizationAdmin(admin.ModelAdmin):
    pass


admin.site.register(User, MyUserAdmin)
admin.site.register(Organization, OrganizationAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Permission, PermissionAdmin)
