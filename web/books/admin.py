from django.contrib import admin

# Register your models here.

from .models import Book


class BookAdmin(admin.ModelAdmin):
    pass


admin.site.register([Book], BookAdmin)
