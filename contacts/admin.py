from django.contrib import admin
from .models import Contact
# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_display = ('id','deal_id', 'deal_type','first_name', 'last_name', 'customer', 'deal_type','address','email','phone', 'create_date')
    list_display_links = ('deal_id', 'first_name','last_name')
    search_fields = ('first_name','last_name','email','deal_type','address')
    list_per_page = 25



admin.site.register(Contact, ContactAdmin)