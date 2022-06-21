from django.shortcuts import render
from .models import Registration
from .forms import RegForm
from django.http import HttpResponseRedirect
# Create your views here.
def home(request):
    return render(request,'home.html')
def form_view(request):
    submitted=False
    if request.method == 'POST':
        form=RegForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/form?submitted=True')
    else:
        form=RegForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request,'registration.html',{'form':form,'submitted':submitted})
