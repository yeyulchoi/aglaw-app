from django.shortcuts import render
from .models import Team
from transactions.models import Transaction

# Create your views here.
def home(request):
    teams =Team.objects.all()
    today_closings =Transaction.objects.order_by('closing_date').filter(is_deal_closed=True)
    weekly_closings=Transaction.objects.order_by('closing_date')
    data={
        'teams': teams,
        'today_closings':today_closings,
        'weekly_closings':weekly_closings,
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