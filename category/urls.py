from django.urls import path
from . import views

urlpatterns = [
    path('',views.Catagory_Main, name='category'),
    path('category_create',views.category_create, name='category_create'),
    path('category_store',views.category_store, name='category_store'),
    path('category_delete/<int:id>', views.category_delete, name='category_delete'),
    path('category_edit/<int:id>', views.category_edit, name='category_edit'),
    path('category_update/<int:id>', views.category_update, name='category_update'),
    
]