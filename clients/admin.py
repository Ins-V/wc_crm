from django.contrib import admin

from clients.models import Phone, Email, Company


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    search_fields = ['name']
    readonly_fields = ('created', 'updated')
    fieldsets = (
        (None, {
            'fields': ('name', 'description')
        }),
        ('Контакты', {
            'fields': ('contact_person', 'address', 'phones', 'emails'),
        }),
        ('Даты', {
            'fields': ('created', 'updated',),
        }),
    )
    filter_horizontal = ('phones', 'emails')
    save_on_top = True


admin.site.register(Phone)
admin.site.register(Email)
