from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, HttpResponse
from django.urls import reverse, reverse_lazy

from .models import Person, Subject, Group, Result
from .forms import ContactForm, GroupForm, ResultForm
from django.core.mail import send_mail
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView
from django.views.generic.base import ContextMixin


# Create your views here.
def main_page(request):
    persons = Person.objects.all()
    return render(request, 'educenterapp/index.html', context={'persons': persons})


def create_person(request):
    if request.method == 'POST':
        form = ContactForm(request.POST, files=request.FILES)
        if form.is_valid():
            name = form.cleaned_data['name']
            bday = form.cleaned_data['bday']
            email = form.cleaned_data['email']
            photo = form.cleaned_data['photo']
            send_mail(
                'Регистрация',
                f' {name} {bday} Вы зарегистрированы.',
                'from@educenter.com',
                [email],
                fail_silently=True,
            )
            Person.objects.create(name=name, bday=bday, email=email, photo=photo)
            return HttpResponseRedirect(reverse('educenter:index'))
        else:
            return render(request, 'educenterapp/create.html', context={'form': form})
    else:
        form = ContactForm()
        return render(request, 'educenterapp/create.html', context={'form': form})

def person(request, id):
    person = Person.objects.get(id=id)
    return render(request, 'educenterapp/person.html', context={'person':person})

# def subject(request):
#     subjects = Subject.objects.all()
#     return render(request, 'educenterapp/subject.html', context={'subjects': subjects})

def group(request):
    if request.method == 'POST':
        form = GroupForm(request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('educenter:index'))
        else:
            return render(request, 'educenterapp/group.html', context={'form': form})
    else:
        form = GroupForm()
        return render(request, 'educenterapp/group.html', context={'form': form})


def result(request):
    if request.method == 'POST':
        form = ResultForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('educenter:index'))
        else:
            return render(request, 'educenterapp/result.html', context={'form': form})
    else:
        form = ResultForm()
        return render(request, 'educenterapp/result.html', context={'form': form})

class NameContextMixin(ContextMixin):
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['name'] = 'Предметы/Группы'
        return context

class SubjectListView(ListView, NameContextMixin):
    model = Subject
    template_name = 'educenterapp/subject_list.html'
    context_object_name = 'Предметы'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['name'] = 'Предметы'
        return context

    def get_queryset(self):
        return Subject.objects.all()

class SubjectDetailView(DetailView, NameContextMixin):
    model = Subject
    template_name = 'educenterapp/subject_detail.html'

    def get(self, request, *args, **kwargs):
        self.subject_id = kwargs['pk']
        return super().get(request, *args, **kwargs)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['name'] = 'Предмет'
        return context

    def get_object(self, queryset=None):
        return get_object_or_404(Subject, pk=self.subject_id)

class SubjectCreateView(CreateView):
    fields = '__all__'
    model = Subject
    template_name = 'educenterapp/subject_create.html'
    success_url = reverse_lazy('educenter:subject_list')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['name'] = 'Предмет'
        return context

    def form_valid(self, form):
        return super().form_valid(form)

    def post(self, request,  *args, **kwargs):
        return super().post(request, *args, **kwargs)


class SubjectDeleteView(DeleteView):
    fields = '__all__'
    model = Subject
    template_name = 'educenterapp/subject_delete_confirm.html'
    success_url = reverse_lazy('educenter:subject_list')


class SubjectUpdateView(UpdateView):
    fields = '__all__'
    model = Subject
    template_name = 'educenterapp/subject_create.html'
    success_url = reverse_lazy('educenter:subject_list')

class GroupListView(ListView, NameContextMixin):
    model = Group
    template_name = 'educenterapp/group_list.html'
    context_object_name = 'Группы'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['name'] = 'Группы'
        return context

    def get_queryset(self):
        return Group.objects.all()


class GroupDetailView(DetailView, NameContextMixin):
    model = Group
    template_name = 'educenterapp/group_detail.html'

    def get(self, request, *args, **kwargs):
        self.group_id = kwargs['pk']
        return super().get(request, *args, **kwargs)
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['name'] = 'Группа'
        context['persons'] = Person.objects.all()
        return context

class GroupCreateView(CreateView):
    fields = '__all__'
    model = Group
    template_name = 'educenterapp/group_create.html'
    success_url = reverse_lazy('educenter:group_list')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['name'] = 'Группа'
        return context

    def form_valid(self, form):
        return super().form_valid(form)

    def post(self, request,  *args, **kwargs):
        return super().post(request, *args, **kwargs)


class GroupDeleteView(DeleteView):
    fields = '__all__'
    model = Group
    template_name = 'educenterapp/group_delete_confirm.html'
    success_url = reverse_lazy('educenter:group_list')


class GroupUpdateView(UpdateView):
    fields = '__all__'
    model = Group
    template_name = 'educenterapp/group_create.html'
    success_url = reverse_lazy('educenter:group_list')


class ResultListView(ListView, NameContextMixin):
    model = Result
    template_name = 'educenterapp/result_list.html'
    context_object_name = 'Предметы'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['name'] = 'Предметы'
        return context

    def get_queryset(self):
        return Result.objects.all()

class ResultDetailView(DetailView, NameContextMixin):
    model = Result
    template_name = 'educenterapp/result_detail.html'

    def get(self, request, *args, **kwargs):
        self.result_id = kwargs['pk']
        return super().get(request, *args, **kwargs)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['name'] = 'Предмет'
        return context

    def get_object(self, queryset=None):
        return get_object_or_404(Result, pk=self.result_id)

class ResultCreateView(CreateView):
    fields = '__all__'
    model = Result
    template_name = 'educenterapp/result_create.html'
    success_url = reverse_lazy('educenter:result_list')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['name'] = 'Предмет'
        return context

    def form_valid(self, form):
        return super().form_valid(form)

    def post(self, request,  *args, **kwargs):
        return super().post(request, *args, **kwargs)


class ResultDeleteView(DeleteView):
    fields = '__all__'
    model = Result
    template_name = 'educenterapp/result_delete_confirm.html'
    success_url = reverse_lazy('educenter:result_list')


class ResultUpdateView(UpdateView):
    fields = '__all__'
    model = Result
    template_name = 'educenterapp/result_create.html'
    success_url = reverse_lazy('educenter:result_list')



