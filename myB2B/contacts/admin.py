from django.contrib import admin
from .models import BasicContact


class BasicContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'country', 'phone', 'created_on')
    list_display_links = ('id', 'email',)


admin.site.register(BasicContact, BasicContactAdmin)
