from django.urls import path, include
from .import views


urlpatterns = [

    path('',views.loan_list, name='Home'),
    path('tickets/', views.ticket_list, name='Multas')


]