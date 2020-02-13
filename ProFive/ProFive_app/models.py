from django.db import models
from django.contrib.auth.models import User


class UserProfileInfo(models.Model):
    """ User profile default inherited from the django contrib and extended """

    user = models.OneToOneField(User, on_delete=models.PROTECT)
    #added fields
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)

    def str(self):
        return self.user.user.username

class BankAccount(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    bankName = models.CharField(max_length = 100)
    accountNameUser = models.CharField(max_length = 100)
    ibanAccount = models.CharField(max_length = 100)


    def str(self):
        return 'Account "{}": iban {}, bank {}'.format(self.accountNameUser, self.ibanAccount, self.bankName)



class UserLoginInfo(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    loginInfo = models.DateTimeField()
