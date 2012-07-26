from blog.models import Entry
from django.contrib import admin

class EntryAdmin(admin.ModelAdmin):
    search_fields = ["title", "content"]

admin.site.register(Entry, EntryAdmin)

