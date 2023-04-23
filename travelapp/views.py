from django.shortcuts import redirect, render
from travelapp.forms import AddPeopleForm,UpdatePeopleForm,UserRegistrationForm
from travelapp.models import People
from django.contrib.auth.decorators import login_required

def index_view(request):
    return render(request,'travelapp/index.html')

@login_required
def add_view(request):
    obj = AddPeopleForm()
    if request.method == 'POST' :
        obj = AddPeopleForm(request.POST)
    if obj.is_valid():
        obj.save()
        return redirect('/travel/list/')

    return render(request, 'travelapp/add.html', {'obj': obj})

@login_required
def list_view(request):
   data = People.objects.all()
   return render(request, 'travelapp/list.html', {'data': data})

@login_required
def detail_view(request, id):
    obj = People.objects.get(pk = id)
    return render(request, 'travelapp/detail.html', {'obj':obj}) 

@login_required
def update_view(request, id):
    obj = People.objects.get(pk = id)
    form = UpdatePeopleForm(instance=obj)
    if request.method == 'POST' :
        form = UpdatePeopleForm(request.POST, instance= obj)
        if form.is_valid():
            form.save()
            return redirect(f'/travel/detail/{obj.id}/')
    
    return render(request, 'travelapp/update.html', {'obj':obj , 'form':form})      

@login_required
def delete_view(request, id):
    obj = People.objects.get(pk = id)
    obj.delete()
    return redirect('/travel/list/')    

@login_required
def a_view(request):
    return render(request, 'travelapp/a.html') 

@login_required
def b_view(request):
    return render(request, 'travelapp/b.html')

@login_required
def c_view(request):
    return render(request, 'travelapp/c.html') 

@login_required
def d_view(request):
    return render(request, 'travelapp/d.html') 

@login_required
def e_view(request):
    return render(request, 'travelapp/e.html')         
    
def register_view(request):
    form = UserRegistrationForm()
    print(request.POST)
    if request.method == 'POST' :
        form = UserRegistrationForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('/login/')
    return render(request, 'travelapp/register.html', {'form':form})