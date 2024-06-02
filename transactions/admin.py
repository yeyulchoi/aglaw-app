from django.contrib import admin
from .models import Transaction
from django.utils.html import format_html
# Register your models here.

class TransactionAdmin(admin.ModelAdmin):
    def thumbnail(self,object):
        return format_html('<img src="{}"  width="30" style=border-radius: 50px/>'.format(object.client_photo1.url))

    thumbnail.short_description = 'Photo'
    list_display = ('file_number','thumbnail','deal_type','client_name','price','email','phone','is_deal_closed','created_date',)
    list_display_links = ('file_number','thumbnail','client_name')
    list_editable = ('is_deal_closed',)
    search_fields = ('file_number', 'client_name')
    list_filter=('file_number','client_name','is_deal_closed')




admin.site.register(Transaction, TransactionAdmin)
