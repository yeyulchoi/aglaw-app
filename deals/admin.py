from django.contrib import admin
from .models import Deal
from django.utils.html import format_html
# Register your models here.

class DealAdmin(admin.ModelAdmin):
    # def thumbnail(self,object):
    #     return format_html('<img src="{}"  width="30" style=border-radius: 50px/>'.format(object.client_photo1.url))

    # thumbnail.short_description = 'Photo'
    list_display = ('deal_id','file_number','client_name','deal_type','closing_date', 'status','price','unit_number','street_number','street_name','street_suffix','city','is_deal_closed')
    list_display_links = ('file_number','client_name')
    list_editable = ('is_deal_closed',)
    search_fields = ('file_number', 'client_name','deal_type')
    list_filter=('file_number','client_name','is_deal_closed','deal_type')




admin.site.register(Deal, DealAdmin)
