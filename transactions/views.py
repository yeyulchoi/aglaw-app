from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from .models import Transaction
from django.core.paginator import EmptyPage, PageNotAnInteger

# Create your views here.

def transactions(request):
    all_deals=Transaction.objects.order_by('-created_date')
    paginator =Paginator(all_deals,4)
    page = request.GET.get('page')
    paged_deals=paginator.get_page(page)


    deal_types = Transaction.objects.values_list('deal_type', flat=True).distinct()
    cities = Transaction.objects.values_list('city', flat=True).distinct()
    provinces = Transaction.objects.values_list('province', flat=True).distinct()
    data = {
        'all_deals':paged_deals,
        'deal_types': deal_types,
        'cities': cities,
        'provinces': provinces,


    }
    return render(request,'transactions/transactions.html', data)


def deal_detail(request,file_number):
    single_deal= get_object_or_404(Transaction,pk=file_number)

    data={
        'single_deal':single_deal,
    }
    return render(request, 'transactions/deal_detail.html', data)

def search(request):
    deals = Transaction.objects.order_by('-created_date')

    deal_types = Transaction.objects.values_list('deal_type', flat=True).distinct()
    cities = Transaction.objects.values_list('city', flat=True).distinct()
    provinces = Transaction.objects.values_list('province', flat=True).distinct()



    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            deals = deals.filter(client_name__icontains=keyword)

    if 'city' in request.GET:
        city=request.GET['city']
        if city:
            deals =deals.filter(city__iexact=city)

    if 'dealtype' in request.GET:
        dealtype=request.GET['dealtype']
        if dealtype:
            deals =deals.filter(deal_type__iexact=dealtype)

    if 'province' in request.GET:
        province=request.GET['province']
        if province:
            deals =deals.filter(province__iexact=province)

    if 'min_price' in request.GET and 'max_price' in request.GET:

        min_price = request.GET['min_price']
        max_price = request.GET['max_price']
        if max_price:
            deals =deals.filter(price__gte=min_price, price__lte=max_price)
    data={
        'deals':deals,
        'deal_types': deal_types,
        'cities': cities,
        'provinces': provinces,
    }
    return render(request,'transactions/search.html', data)