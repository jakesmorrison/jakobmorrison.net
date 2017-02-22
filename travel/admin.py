from django.contrib import admin

# Register your models here.

class CreditCardModelAdmin(admin.ModelAdmin):
    list_display= "self.cc_id,self.issuer,self.card,self.date_approved,self.bonus_recieved," \
                  "self.bonus,self.min_spend,self.fee,self.line".replace("self.","").split(",")
    search_fields = list_display
from .models import CreditCard
admin.site.register(CreditCard, CreditCardModelAdmin)

class UserModelAdmin(admin.ModelAdmin):
    list_display = ["user_id","name","email"]
    search_fields = list_display
from .models import User
admin.site.register(User,UserModelAdmin)

class IssuedModelAdmin(admin.ModelAdmin):
    list_display = ["issue_id","cc_id","user_id"]
    search_fields = list_display
from .models import Issued
admin.site.register(Issued,IssuedModelAdmin)