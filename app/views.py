from django.shortcuts import redirect, render
from .forms import usuariosForm
from .models import usuarios
from django.contrib.auth.models import User


def home(request):
    data = {}    
    search = request.GET.get('search')
    if search:
        data['db'] = usuarios.objects.filter(login__icontains=search)
    else:
        data['db'] = usuarios.objects.all()
    #all = Carros.objects.all()
    #paginator = Paginator(all, 2)
    #pages = request.GET.get('page')
    #data['db'] = paginator.get_page(pages)
    return render(request, 'main.html', data)

def form(request):
    data = {}
    data['form'] = usuariosForm()
    return render(request, 'create.html', data)

def create(request):
    if request.method == "POST":
        form = usuariosForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            if obj.password == '' or obj.password is None:
                obj.password  = User.objects.make_random_password()
            obj.save()
    form = usuariosForm()
    return render(request, 'create.html', {'form': form})

def edit(request, pk):
    data = {}
    data['db'] = usuarios.objects.get(pk=pk)
    data['form'] = usuariosForm(instance=data['db'])
    return render(request, 'create.html', data)

def update(request, pk):
    data = {}
    data['db'] = usuarios.objects.get(pk=pk)
    form = usuariosForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('home')

def delete(request, pk):
    db = usuarios.objects.get(pk=pk)
    db.delete()
    return redirect('home')
