from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('search_list/',views.search_list,name="search_list"),
    path('search/',views.search,name="search"),
    path('product/<int:myid>',views.productView,name="prodview"),
    path('consumed/',views.consumed,name="consumed"),
]
