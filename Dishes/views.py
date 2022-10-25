from django.shortcuts import render,redirect
from django.views.generic import View,ListView,DetailView,DeleteView,UpdateView
from Dishes.models import Dishes
from Dishes.forms import RegistrationForm,LoginForm,DishUpdateForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy

# Create your views here.

def signin_required(fn):
    def wrapper(request,*args,**kwargs):
        if not request.user.is_authenticated:
            messages.error(request,"You must login")
            return redirect("signin")
        else:
            return fn(request,*args,**kwargs)
    return wrapper

@method_decorator(signin_required,name="dispatch")
class Add_Dishes_View(View):

    def get(self,request,*args,**kwargs):
        return render(request,"add_dish.html")

    def post(self,request,*args,**kwargs):
        name = request.POST.get("name")
        user = request.user
        category = request.POST.get("category")
        price = request.POST.get("price")
        rating = request.POST.get("rating")
        Dishes.objects.create(user=request.user,name=name,category=category,price=price,rating=rating)
        messages.success(request,"Dish has been created")
        return redirect("dish-list")

@method_decorator(signin_required,name="dispatch")
class Dish_List_View(ListView):
    model = Dishes
    template_name = "list_dishes.html"
    context_object_name = "dishes"

    def get_queryset(self):
        return Dishes.objects.filter(user = self.request.user)

    # def get(self,request,*args,**kwargs):
    #     if request.user.is_authenticated:

    #         qs = Dishes.objects.filter(user=request.user)
    #         return render(request,"list_dishes.html",{"dishes":qs})
    #     else:
    #         return redirect("signin")

@method_decorator(signin_required,name="dispatch")
class Dish_Detail_View(DetailView):
    model = Dishes
    template_name = "dish-detail.html"
    context_object_name = "dish"
    pk_url_kwarg = "id"
    # def get(self,request,*args,**kwargs):
    #     id = kwargs.get("id")
    #     dish = Dishes.objects.get(id=id)
    #     return render(request,"dish-detail.html",{"dish":dish})        

@method_decorator(signin_required,name="dispatch")
class Dish_Delete_View(DeleteView):
    def get(self,request,*args,**kwargs):
        id = kwargs.get("id")
        Dishes.objects.get(id=id).delete()
        messages.success(request,"Dish deleted")
        return redirect("dish-list")

class RegistrationView(View):
    def get(self,request,*args,**kwargs):
        form = RegistrationForm()
        return render(request,"register.html",{"form":form})

    def post(self,request,*args,**kwargs):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            User.objects.create_user(**form.cleaned_data)
            messages.success(request,"Account created")
            return redirect("dish-list")
        else:
            messages.error(request,"Registration failed")
            return render(request,"register.html",{"form":form})

class LoginView(View):
    def get(self,request,*args,**kwargs):
        form = LoginForm()
        return render(request,"login.html",{"form":form})

    def post(self,request,*args,**kwargs):
        form = LoginForm(request.POST)
        if form.is_valid():
            uname = form.cleaned_data.get("username")
            pwd = form.cleaned_data.get("password")
            usr = authenticate(request,username=uname,password=pwd)
            if usr:
                login(request,usr)
                return redirect("dish-list")
            else:
                messages.error(request,"Invalid credentials")
                return render(request,"login.html",{"form":form})

@signin_required
def signout_view(request,*args,**kwargs):
    logout(request)
    return redirect("register")


class Dish_Update_View(UpdateView):
    model = Dishes
    template_name = "dish-update.html"
    form_class = DishUpdateForm
    pk_url_kwarg = "id"
    success_url = reverse_lazy("dish-list")
