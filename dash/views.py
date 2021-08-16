from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse


from dash.forms import PersonForm, PersonDetailForm
from dash.models import Person


def home(request):
    if request.user.is_authenticated:
        return render(request, "dash/home.html")
    else:
        return HttpResponseRedirect(reverse('login'))

def contacts(request):
    
    if request.user.is_authenticated:
        person_objects = Person.objects.all()
        if request.method == 'POST':
            
            form = PersonForm(request.POST)
            
            if form.errors:
                return render(request, 'dash/contacts.html', {
                    'form' : PersonForm(request.POST),
                    'persons': person_objects
                })
            
            if form.is_valid():
                first_name = form.cleaned_data['first_name']
                email = form.cleaned_data['email']
                phone = form.cleaned_data['phone']
                company = form.cleaned_data['company']
                label = form.cleaned_data['label']
                
                person = Person(first_name=first_name, email=email, phone=phone,
                                company_id=company, label=label)
                person.save()
                
                return HttpResponseRedirect('/dash/contacts')
            
        else:
            return render(request, 'dash/contacts.html', {
                'form' : PersonForm(),
                'persons': person_objects
            })
    else:
        return HttpResponseRedirect(reverse('login'))

def contacts_detail(request, pk):
    detail = Person.objects.get(pk=pk)
    form = PersonDetailForm()
    return render(request, 'dash/contacts_detail.html',{
        'detail':detail,
        'form': form
    })


