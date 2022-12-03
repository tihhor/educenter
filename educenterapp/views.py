from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, HttpResponse
from django.urls import reverse, reverse_lazy
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Person, Subject, Group, Result
from .forms import ContactForm, GroupForm, ResultForm
from django.core.mail import send_mail
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView
from django.views.generic.base import ContextMixin
from django.views.decorators.cache import cache_page



# Create your views here.
def main_page(request):
    # persons = Person.objects.all()
    persons = Person.objects.filter(is_active=True)
    paginator = Paginator(persons, 300)
    page = request.GET.get('page')
    try:
        persons = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        persons = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        persons = paginator.page(paginator.num_pages)
    title = 'классный журнал'

    return render(request, 'educenterapp/index.html', context={'persons': persons, 'title': title})


@login_required(login_url='/test/login/')
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

@user_passes_test(lambda u:u.is_superuser, login_url='/test/login/')
def person(request, id):
    person = Person.objects.get(id=id)
    all_subjects = person.get_all_subj
    for item in all_subjects:
        print(item.name)
    return render(request, 'educenterapp/person.html', context={'person':person})


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
            form.instance.user = request.user
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


class GroupDetailView(UserPassesTestMixin, DetailView, NameContextMixin):
    model = Group
    template_name = 'educenterapp/group_detail.html'
    raise_exception = False
    login_url = 'test:login'


    def test_func(self):
        return self.request.user.is_superuser

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


# @cache_page(60)
class ResultListView(ListView, NameContextMixin):
    model = Result
    template_name = 'educenterapp/result_list.html'
    context_object_name = 'Предметы'
    paginate_by = 300

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['name'] = 'Предметы'
        return context

    def get_queryset(self):
        return Result.objects.select_related('subject', 'user', 'person').all()
        # return Result.objects.all()

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

class ResultCreateView(LoginRequiredMixin, CreateView):
    fields = ('person', 'subject','mark' ,)
    model = Result
    template_name = 'educenterapp/result_create.html'
    success_url = reverse_lazy('educenter:result_list')
    login_url = 'test:login'


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['name'] = 'Предмет'
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def post(self, request,  *args, **kwargs):
        return super().post(request, *args, **kwargs)


class ResultDeleteView(DeleteView):
    fields = '__all__'
    model = Result
    template_name = 'educenterapp/result_delete_confirm.html'
    success_url = reverse_lazy('educenter:result_list')


class ResultUpdateView(UpdateView):
    fields = ('person', 'subject', 'mark',)
    model = Result
    template_name = 'educenterapp/result_create.html'
    success_url = reverse_lazy('educenter:result_list')



