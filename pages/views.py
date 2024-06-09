from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.shortcuts import render
from .models import Team
from deals.models import Deal
from django.utils import timezone
from datetime import timedelta
from django.contrib import messages


# Create your views here.
def home(request):
    today=timezone.now().date()
    teams =Team.objects.all()
    deal_types= Deal.objects.values_list('deal_type',flat=True).distinct()
    cities = Deal.objects.values_list('city', flat=True).distinct()
    provinces = Deal.objects.values_list('province', flat=True).distinct()
    all_closings=Deal.objects.all()
    closings =Deal.objects.order_by('-created_date').filter(closing_date__date=today,is_deal_closed=False)
    all_closings =Deal.objects.order_by('-created_date').filter(is_deal_closed=False)
    tomorrow =timezone.now().date() +timedelta(days=1)
    one_week_later = tomorrow+timedelta(days=9)
    two_weeks_closings = Deal.objects.filter(closing_date__date__range=(tomorrow, one_week_later))
    data={
        'teams': teams,
        'deal_types':deal_types,
        'cities':cities,
        'provinces':provinces,
        'closings':closings,
        'all_closing':all_closings,
        'two_weeks_closings':two_weeks_closings,
        'all_closings':all_closings

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
    if request.method=='POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        phone = request.POST['phone']
        message = request.POST['message']

        email_subject = "You have new message re real estate transaction "+subject
        message_body =name+ ';'+  email + ';' +phone + '; '+message



        admin_info = User.objects.get(is_superuser=True)
        admin_email = admin_info.email
        send_mail(
            email_subject,
            message_body,
            "yeyulchoi@gmail.com",
            [admin_email],
            fail_silently=False,
        )

        messages.success(request,"Your messaged has been delivered.")
    return render(request, 'pages/contact.html' )





