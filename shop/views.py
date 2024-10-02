from django.shortcuts import render,redirect
from .models import Product,Category
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .forms import SignUpForm, UpdateUserForm ,UpdatePasswordForm

def category_summery(request):
        all_cat =Category.objects.all()
        return render(request, 'category_summery.html',{'category':all_cat})


def helloworld(request):
    all_products = Product.objects.all()
    return render(request, 'home.html',{'products':all_products})

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')



def login_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password =request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request,("با موفقیت وارد شدید"))
            return redirect("home")
        else:
            messages.success(request,("نام کاربری یا پسورد اشتباه است"))
            return redirect("login")
    else:
     return render(request, 'login.html')


def logout_user(request):
    logout(request)
    messages.success(request,("با موفقیت خارج شدید"))
    return redirect("home")




def signup_user(request): 
    form = SignUpForm() 
    if request.method == "POST": 
        form = SignUpForm(request.POST) 
        if form.is_valid(): 
            user = form.save()  # Save the user instance
            username = form.cleaned_data.get('username') 
            password = form.cleaned_data.get('password') 
            user = authenticate(request, username=username, password=password) 
            if user is not None:  # Check if user is authenticated
                login(request, user) 
                messages.success(request, 'ثبت نام با موفقیت انجام شد.') 
                return redirect("home") 
            else:
                messages.error(request, 'ثبت نام با موفقیت انجام شد') 
                return redirect("signup") 
        else: 
            messages.error(request, 'ثبت نام با موفقیت انجام شد') 
            return redirect("signup") 
    else: 
        return render(request, 'signup.html', {'form': form})
    


def update_user(request):
    if request.user.is_authenticated:
        current_user = User.objects.get(id=request.user.id)
        user_form = UpdateUserForm(request.POST or None, instance = current_user)
        if user_form.is_valid():
            user_form.save()
            login(request, current_user)
            messages.success(request, 'پروفایل شما ویرایش شد')
            return redirect ('home')
        return render(request, 'update_user.html',{'user_form': user_form})   
    else:
        messages.success(request, 'ابتدا باید لاگین شوید')
        return redirect ('home')



def update_password(request):
    if request.user.is_authenticated:
        current_user = request.user
        if request.method == 'POST':
            form = UpdatePasswordForm(current_user, request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'رمز با موفقیت ویرایش شد')
                login(request, current_user)
                return redirect('update_user')
            else:
                for error in list(form.errors.values()):
                    messages.error(request, error)
                return redirect('update_password')
        else:
            form = UpdatePasswordForm(current_user)
            return render(request, 'update_password.html',{'form': form})
    else:
        messages.success(request,'باید اول لاگین شوید')
        return redirect ('home')





def product(request,pk):
    product = Product.objects.get(id=pk)
    return render(request, 'product.html ', {'product':product})





    
def category(request,cat):
    cat=cat.replace("-",' ')
    try:
        category = Category.objects.filter(name=cat).first()
        products = Product.objects.filter(Category_id=category.id).all()
        return render(request,'category.html',{'products':products,'category':category})
    except:
        messages.success(request,('دسته بندی وجود ندارد'))
        return redirect("home")
                    
    





