from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact
from django.core.mail import send_mail
from django.contrib.auth.models import User

# Create your views here.
def inquiry(request):

    if request.method=="POST":
        user_id = request.POST.get('user_id', None)
        deal_id = request.POST['deal_id']
        deal_type = request.POST['deal_type']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        customer = request.POST['customer']
        address = request.POST['address']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']


        contact =Contact(deal_id=deal_id,
                         deal_type=deal_type,
                         user_id=user_id,
                         first_name=first_name,
                         last_name=last_name,
                         customer=customer,
                         address=address,
                         email=email,
                         phone=phone,
                         message=message
                         )




        admin_info =User.objects.get(is_superuser=True)
        admin_email =admin_info.email
        send_mail(
            "Transaction Inquiry",
            "I am " +customer+ "and have an inquiry for the transaction "+ contact.deal_type+" for "+ contact.address +". My message :"+contact.message,
            "yeyulchoi@gmail.com",
            [admin_email],
            fail_silently=False,
        )

    contact.save()
    messages.success(request, 'Your request has been submitted, we will contact you shortly.')
    return redirect('/deals/'+deal_id)