import json

from django.http import HttpResponse
from django.shortcuts import render
import requests
from django.urls import reverse, reverse_lazy

from django.views.generic import DetailView, ListView, CreateView, View

from .forms import ContactForm
from .models import Contacts


class ListContactView(ListView):
    """List all contacts in db"""
    model = Contacts
    template_name = "list.html"
    ordering = ['-id']



class CreateContactView(CreateView):
    """Creates a new contact"""
    model = Contacts
    form_class = ContactForm
    template_name = "create.html"
    success_url = reverse_lazy('contact:list')

    def get_form_kwargs(self):
        kwargs = super(CreateContactView, self).get_form_kwargs()
        response = requests.get('https://sigma-studios.s3-us-west-2.amazonaws.com/test/colombia.json')
        states = list(response.json().keys())
        print(states)
        kwargs['state'] = states
        return kwargs


class GetCities(View):
    def get(self, request):
        state = request.GET['state']
        print(state)
        response = requests.get('https://sigma-studios.s3-us-west-2.amazonaws.com/test/colombia.json')
        cities = response.json().pop(state)
        print(cities)
        return HttpResponse(json.dumps(cities), content_type='application/json')