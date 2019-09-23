from django.contrib import admin
from .models import Role, Activity, Process, Product
# Register your models here.


class RoleAdmin(admin.ModelAdmin):
    pass


class ActivityAdmin(admin.ModelAdmin):
    pass


class ProcessAdmin(admin.ModelAdmin):
    pass


class ProductAdmin(admin.ModelAdmin):
    pass


admin.site.register(Role, RoleAdmin)
admin.site.register(Activity, ActivityAdmin)
admin.site.register(Process, ProcessAdmin)
admin.site.register(Product, ProductAdmin)
