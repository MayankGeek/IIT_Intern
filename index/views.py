from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm
from django.contrib import messages
from .forms import ImageForm

def home(request):
    return render(request,'index/home.html')



def register(request):
    if request.method=='POST':
         form=UserRegisterForm(request.POST)
         if form.is_valid():
             form.save()
             username=form.cleaned_data.get('username')
             messages.success(request,f'Hi {username},your account was created successfully')
             return redirect('login')
    else:
        form=UserRegisterForm()

    return render(request,'index/register.html',{'form':form})


def login(request):
    return render(request,'index/login.html')



def logout(request):
    return render(request,'index/login.html')




def image_upload_view(request):
    """Process images uploaded by users"""
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Get the current instance object to display in the template
            img_obj = form.instance
            return render(request, 'index/index.html', {'form': form, 'img_obj': img_obj})
    else:
        form = ImageForm()
    return render(request, 'index/index.html', {'form': form})
