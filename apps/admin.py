from django.contrib import admin

from apps.models import Contact


@admin.register(Contact)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name','image')
