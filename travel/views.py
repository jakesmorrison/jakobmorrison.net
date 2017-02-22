from django.shortcuts import render
from .models import CreditCard, User, Issued

# Create your views here.

def home(request):
    (cc_instance, new_cc) = CreditCard.objects.update_or_create(
        cc_id = "ccid_3",
        issuer = "AMEX",
        card = "Premium",
        date_approved = "2016-04-13",
        bonus_recieved = "2016-07-13",
        bonus = "50000",
        min_spend = "3000",
        fee = "95",
        line = "10000"
    )

    (user_instance, new_user) = User.objects.update_or_create(
        user_id = "userid_54",
        name = "Jake Morrison",
        email = "jakesmorrison4@gmail.com"
    )

    (issued_instance, new_issued) = Issued.objects.update_or_create(
        issue_id = "issuedid_24",
        cc_id = cc_instance,
        user_id = user_instance
    )

    context = {

    }
    return render(request, 'travel/home.html', context)