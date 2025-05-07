from django.contrib import admin
from django.urls import path
from MainApp import views

urlpatterns = [

    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('item/<int:item_id>/', views.show_item, name='show_item'), 
    path('items/', views.item_list, name='item_list'),
    
]