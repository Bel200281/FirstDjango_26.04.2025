from django.contrib import admin
from django.urls import path
from MainApp import views
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('about/', views.about),
    path('item/<int:item_id>/', views.show_item),
    path('items/', views.item_list),

    path('item/<int:item_id>/', views.show_item, name='item'),
]