from django.contrib import admin
from dash.models import Person


class PersonAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'label', 'email', 'phone',
                    'company_id', 'update_date', 'created_date']
    list_display_links = ['id', 'first_name']
    search_fields = ['first_name', 'last_name', 'label']
    ordering = ['id']

admin.site.register(Person, PersonAdmin)