from django.contrib import admin

from clients.models import Phone, Email, Company


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    pass


admin.site.register(Phone)
admin.site.register(Email)
