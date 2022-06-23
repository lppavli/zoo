from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from .models import Animal
from .tasks import send_mail_task
from .forms import ContactForm, AnimalForm, RegistrationForm, LoginForm
from celery import current_app
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView, FormView


class AdminOnlyMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_superuser


class StaffOnlyMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_staff


class AnimalListView(ListView):
    model = Animal
    template_name = 'animals/index.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['active_page'] = '/'
        return context


class AnimalDetailView(AdminOnlyMixin, DetailView):
    model = Animal
    template_name = 'animals/animal.html'


class AnimalCreateView(StaffOnlyMixin, CreateView):
    model = Animal
    template_name = 'animals/edit.html'
    success_url = '/'
    # fields = '__all__'
    form_class = AnimalForm


class AnimalUpdateView(UpdateView):
    model = Animal
    template_name = 'animals/edit.html'
    success_url = '/'
    # fields = '__all__'
    form_class = AnimalForm

    def form_valid(self, form):
        user = self.request.user
        form.instance.user = user
        return super(AnimalUpdateView, self).form_valid(form)


class AnimalDeleteView(DeleteView):
    model = Animal
    success_url = '/'
    template_name = 'animals/delete_confirm.html'


class UserCreateView(CreateView):
    model = User
    form_class = RegistrationForm
    success_url = '/'
    template_name = 'animals/register.html'


class LoginUserView(LoginView):
    form_class = LoginForm
    success_url = '/'
    template_name = 'animals/login.html'

class LogoutUserView(LogoutView):
    pass


def status_view(request):
    task_id = request.GET['task_id']
    # По id получить задачу
    task = current_app.AsyncResult(task_id)
    status = task.status
    return render(request, 'animals/status.html', {'status': status, 'task_id': task.id})

# только для залогиненного
class ContactFormView(LoginRequiredMixin, FormView):
    template_name = 'animals/contact.html'
    form_class = ContactForm
    success_url = '/'

    def form_valid(self, form):
        subject = form.cleaned_data['subject']
        text = form.cleaned_data['message']
        email = form.cleaned_data['email']
        send_mail_task.delay(subject, text, email)
        return super().form_valid(form)
