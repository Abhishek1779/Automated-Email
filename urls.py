from django.urls import path
from . import views
urlpatterns = [
    path('',views.data,name='enter_data'),
    path('confirm_mail',views.sendmail,name='send_mail')
]