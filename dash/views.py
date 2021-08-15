from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages

from dash.forms import PersonForm
from dash.models import Person


def home(request):
    if request.user.is_authenticated:
        return render(request, "dash/home.html")
    else:
        return HttpResponseRedirect(reverse('login'))

def contacts(request):
    
    if request.user.is_authenticated:
        if request.method == 'POST':
            
            form = PersonForm(request.POST)
            
            if form.errors:
                return render(request, 'dash/contacts.html', {
                    'form' : PersonForm(request.POST),
                })
            
            if form.is_valid():
                first_name = form.cleaned_data['first_name']
                last_name = form.cleaned_data['last_name']
                email = form.cleaned_data['email']
                birthday = form.cleaned_data['birthday']
                phone = form.cleaned_data['phone']
                company = form.cleaned_data['company']
                label = form.cleaned_data['label']
                
                person = Person(first_name=first_name, last_name=last_name,
                                email=email, birthday=birthday, phone=phone,
                                company_id=company, label=label)
                person.save()
                
                return HttpResponseRedirect('/dash/contacts')
        else:
            person_objects = Person.objects.all()
            return render(request, 'dash/contacts.html', {
                'form' : PersonForm(),
                'persons': person_objects
            })
    else:
        return HttpResponseRedirect(reverse('login'))


