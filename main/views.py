from django.shortcuts import render, redirect
from .models import Category, Product
from main.forms import ProductForm, CategoryForm, UserForm
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate


def IndexView(request):
    return render(request, 'main/index.html')


def AddProductView(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Add product succes")
        else:
            messages.error(request, form.errors)
            # messages.debug
            # messages.success
            # messages.error
            # messages.warning
            # messages.info
    else:
        form = ProductForm()
    context = {
        "form": form
        }
    return render(request, 'main/addproduct.html', context=context)


def ProductView(request):
    products = Product.objects.all()
    context = {
        "products": products
        }
    return render(request, 'main/product.html', context=context)


def CategoryView(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Add category success')
        else:
            messages.success(request, form.errors)
    else:
        form = CategoryForm()
    product = Category.objects.all()
    context = {
        "form": form,
        'product': product
        }
    return render(request, 'main/category.html', context=context,)


def LogoutUserView(request):
    logout(request)
    return redirect('/') 


def SignUpUserView(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            if user.password != request.POST.get('password2'):
                messages.error(request, 'Пароли не совпадают')
                return redirect('/signup')
            else:
                user.set_password(user.password)
                form.save()
                messages.success(request, 'Регистрация прошла успешно')
                redirect('/')
    else:
        form = UserForm()
    return render(request, 'AuthenticateUser/singup.html', {'form': form})


def SignInUserView(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        if username and password:
            try:
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'Вы успешно вошли!')
                    return redirect("/")
                else:
                    messages.error(request, 'Неверное имя пользователя или пароль.')
            except Exception as e:
                messages.error(request, 'Произошла ошибка при аутентификации. Пожалуйста, попробуйте снова.')
        else:
            messages.error(request, 'Пожалуйста, введите имя пользователя и пароль.')
    
    return render(request, "AuthenticateUser/signin.html")
