from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.urls import reverse

from .models import Person
from .forms import ContactForm
from django.core.mail import send_mail


# Create your views here.
def main_page(request):
    persons = Person.objects.all()
    return render(request, 'educenterapp/index.html', context={'persons': persons})


def create_person(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            bday = form.cleaned_data['bday']
            email = form.cleaned_data['email']
            # photo = form.cleaned_data['photo']
            send_mail(
                'Регистрация',
                f' {name} {bday} Вы зарегистрированы.',
                'from@educenter.com',
                [email],
                fail_silently=True,
            )
            Person.objects.create(name=name, bday=bday, email=email)
            return HttpResponseRedirect(reverse('educenter:index'))
        else:
            return render(request, 'educenterapp/create.html', context={'form': form})
    else:
        form = ContactForm()
        return render(request, 'educenterapp/create.html', context={'form': form})

def person(request, id):
    person = Person.objects.get(id=id)
    return render(request, 'educenterapp/person.html', context={'person':person})
