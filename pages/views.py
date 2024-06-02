from django.shortcuts import render
from .models import Team
from transactions.models import Transaction

# Create your views here.
def home(request):
    teams =Team.objects.all()
    deal_types= Transaction.objects.values_list('deal_type',flat=True).distinct()
    cities = Transaction.objects.values_list('city', flat=True).distinct()
    provinces = Transaction.objects.values_list('province', flat=True).distinct()
    closings =Transaction.objects.order_by('-created_date').filter(is_deal_closed=True)

    data={
        'teams': teams,
        'deal_types':deal_types,
        'cities':cities,
        'provinces':provinces,
        'closings':closings,

    }
    return render(request, 'pages/home.html', data)

def about(request):
    teams = Team.objects.all()
    data = {
        'teams': teams,
    }
    return render(request, 'pages/about.html',data)

def services(request):
    return render(request, 'pages/services.html' )

def contact(request):
    return render(request, 'pages/contact.html' )