from typing import Any
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy 

from django.contrib.auth.views import LoginView

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from .models import Task

class CustomLoginView(LoginView):
  template_name = "timer/login.html"
  fields = '__all__'
  redirect_authenticated_user = True

  def get_success_url(self):
    return reverse_lazy('tasks-list')
  

class RegisterPage(FormView): 
   template_name = 'timer/register.html'
   form_class = UserCreationForm
   redirect_authenticated_user = True
   success_url = reverse_lazy('tasks-list')


   def form_valid(self, form):
     user = form.save()
     if user is not None:
        login(self.request, user)
     return super(RegisterPage, self).form_valid(form) 
   
   def get(self,*args, **kwargs):
      if self.request.user.is_authenticated:
        return redirect('tasks-list')
      return super(RegisterPage,self).get(*args, **kwargs)







class Tasklist(LoginRequiredMixin, ListView):
  model = Task
  context_object_name = 'tasks'
  template_name = 'timer/task_list.html'

  def get_context_data(self, **kwargs):
     context = super().get_context_data(**kwargs)
     context['tasks'] = context['tasks'].filter(user=self.request.user)
     context['count'] = context['tasks'].filter(complete=False).count()

     search_input = self.request.GET.get('search-area') or ''
     if search_input:
       context['tasks'] = context['tasks'].filter(title__startswith=search_input)

       context['search_input'] = search_input
        

     return context


class TaskDetail(LoginRequiredMixin, DetailView):
  model = Task
  context_object_name = 'task'
  template_name = 'timer/task.html'

class TaskCreate(LoginRequiredMixin, CreateView):
  model = Task
  fields = ['title','description', 'complete']
  success_url = reverse_lazy('tasks-list')
  template_name = 'timer/task_form.html'

  def form_valid(self, form):
     form.instance.user = self.request.user
     response = super().form_valid(form)
     return redirect('task-update', pk=self.object.pk)
     

  



class TaskUpdate(LoginRequiredMixin, UpdateView):
  model = Task
  fields = ['title','description', 'complete']
  success_url = reverse_lazy('tasks-list')
  template_name = 'timer/task_form.html'

class TaskDelete(LoginRequiredMixin, DeleteView):
  model = Task  # Specify the model
  context_object_name = 'task'
  success_url = reverse_lazy('tasks-list')


