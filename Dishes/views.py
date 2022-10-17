from django.shortcuts import render,redirect
from django.views.generic import View
from Dishes.models import Dishes

# Create your views here.

class Add_Dishes_View(View):

    def get(self,request,*args,**kwargs):
        return render(request,"add_dish.html")

    def post(self,request,*args,**kwargs):
        name = request.POST.get("name")
        category = request.POST.get("category")
        price = request.POST.get("price")
        rating = request.POST.get("rating")
        Dishes.objects.create(name=name,category=category,price=price,rating=rating)
        return render(request,"add_dish.html")

class Dish_List_View(View):
    def get(self,request,*args,**kwargs):
        qs = Dishes.objects.all()
        return render(request,"list_dishes.html",{"dishes":qs})

class Dish_Detail_View(View):
    def get(self,request,*args,**kwargs):
        id = kwargs.get("id")
        dish = Dishes.objects.get(id=id)
        return render(request,"dish-detail.html",{"dish":dish})        

class Dish_Delete_View(View):
    def get(self,request,*args,**kwargs):
        id = kwargs.get("id")
        Dishes.objects.get(id=id).delete()
        return redirect("dish-list")