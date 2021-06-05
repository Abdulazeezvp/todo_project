from django.shortcuts import render,redirect
from .models import Todo_list
from .forms import Todoedit
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView
from django.urls import reverse_lazy

class tasklistview(ListView):
    model = Todo_list
    template_name = 'index.html'
    context_object_name = 'tasks'
class taskdetailview(DetailView):
    model=Todo_list
    template_name = 'detail.html'
    context_object_name = 'i'

class taskupdateview(UpdateView):
    model = Todo_list
    template_name = 'update.html'
    fields = ('task_name','desc','priority','date')
    def get_success_url(self):
        return reverse_lazy('cbvdetail',kwargs={'pk':self.object.id})
class taskdeleteview(DeleteView):
    model = Todo_list
    template_name = 'delete.html'
    success_url = reverse_lazy('cbvhome')
# Create your views here.
def home(request):
    alltasks=Todo_list.objects.all()
    if request.method=='POST':
        name=request.POST.get('name')
        pri=request.POST.get('prioriy')
        desc=request.POST.get('desc')
        date=request.POST.get('date')
        vals=Todo_list(task_name=name,priority=pri,desc=desc,date=date)
        vals.save()
        return redirect('/')
    return render(request,'index.html',{'tasks':alltasks})
def delete(request,taskid):
    task=Todo_list.objects.get(id=taskid)
    if request.method=='POST':
        task.delete()
        return redirect('/')
    return render(request,'delete.html')
def update(request,id):
    data=Todo_list.objects.get(id=id)
    form=Todoedit(request.POST or None,instance=data)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'data':data})

