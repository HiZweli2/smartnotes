from typing import Any
from django.shortcuts import render,redirect
from django.views.generic import ListView,CreateView
from . models import Tasks
from . forms import TodoForm


class NewTask(CreateView):
    model = Tasks
    form_class = TodoForm
    template_name = 'home/home.html'
    success_url = '/'

    def get_context_data(self, **kwargs):
         context = super().get_context_data(**kwargs)
         context["tasks"] = Tasks.objects.all()
         return context
    
def deleteTask(request):
     print('in deleteTask')
     if request.method == 'POST':
          taskID = request.POST.get('taskID')
          print(request.POST.get('taskID'))
          Tasks.objects.get(pk=taskID).delete()
     return redirect("homeView")



    


    

