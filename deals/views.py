from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from .models import Deal
from django.utils.dateparse import parse_date
from django.core.paginator import EmptyPage, PageNotAnInteger

# Create your views here.

def deals(request):
    all_deals=Deal.objects.order_by('-created_date')
    paginator =Paginator(all_deals,4)
    page = request.GET.get('page')
    paged_deals=paginator.get_page(page)


    deal_types = Deal.objects.values_list('deal_type', flat=True).distinct()
    cities = Deal.objects.values_list('city', flat=True).distinct()
    provinces = Deal.objects.values_list('province', flat=True).distinct()
    data = {
        'all_deals':paged_deals,
        'deal_types': deal_types,
        'cities': cities,
        'provinces': provinces,


    }
    return render(request,'deals/deals.html', data)


def deal_detail(request,deal_id):
    single_deal= get_object_or_404(Deal,pk=deal_id)

    data={
        'single_deal':single_deal,
    }
    return render(request, 'deals/deal_detail.html', data)

def search(request):
    deals = Deal.objects.order_by('-created_date')

    deal_types = Deal.objects.values_list('deal_type', flat=True).distinct()
    cities = Deal.objects.values_list('city', flat=True).distinct()
    provinces = Deal.objects.values_list('province', flat=True).distinct()


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

    closing_date_str = request.GET.get('closing_date', '')
    if closing_date_str:
        print("Closing Date String:", closing_date_str)  # Debug line
        closing_date = parse_date(closing_date_str)
        if closing_date:
            print("Parsed Closing Date:", closing_date)  # Debug line
            deals = deals.filter(closing_date__date=closing_date)
        else:
            print("Error parsing closing date:", closing_date_str)  # Debug line

    if 'client_name' in request.GET:
        client_name =request.GET['client_name']
        if client_name:
            deals= deals.filter(client_name__icontains=client_name)
    data={
            'deals':deals,
            'deal_types': deal_types,
            'cities': cities,
            'provinces': provinces,
        }
    return render(request,'deals/search.html', data)