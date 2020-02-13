from django.contrib import admin
from ProFive_app.models import UserProfileInfo, UserLoginInfo,BankAccount
# Register your models here.

admin.site.register(UserLoginInfo)
admin.site.register(UserProfileInfo)
admin.site.register(BankAccount)
