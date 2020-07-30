from django.urls import path

from . import views

app_name = 'contact'

urlpatterns = [
    path('list/', views.ListContactView.as_view(), name='list'),
    path('create/', views.CreateContactView.as_view(), name='create'),
    path('get_cities/', views.GetCities.as_view(), name='cities'),
]
