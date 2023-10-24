from django.urls import path
from . import views

urlpatterns = [
    path('',views.user_main, name='user'),
    path('register',views.register, name='register'),
    path('delete/<int:id>', views.delete, name='delete'),
]
