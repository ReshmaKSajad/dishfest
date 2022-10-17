"""DishFest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Dishes.views import Add_Dishes_View,Dish_List_View,Dish_Detail_View,Dish_Delete_View

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dishes/add/',Add_Dishes_View.as_view(),name="dish-add"),
    path('dishes/list',Dish_List_View.as_view(),name="dish-list"),
    path('dishes/<int:id>/detail',Dish_Detail_View.as_view(),name="dish-detail"),
    path('dishes/<int:id>/delete',Dish_Delete_View.as_view(),name="dish-delete")
]
