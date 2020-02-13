from django.conf.urls import include, url
from ProFive_app import views

# required for templates
app_name = 'ProFive_app'

urlpatterns = [
    url(r'^$', views.login, name='login'),
    url(r'register/$', views.register, name='register'),
    url(r'user_login/$',views.user_login, name='user_login')
]
