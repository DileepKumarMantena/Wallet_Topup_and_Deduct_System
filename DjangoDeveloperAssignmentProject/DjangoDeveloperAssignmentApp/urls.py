from django.urls import path,include
from .views import *


urlpatterns = [
       path('',top_up_request, name='topup'),
       path('top_up_list/',top_up_list, name='top_up_list'),
       path('deduct_amount/',deduct_amount, name='deduct_amount')

]
