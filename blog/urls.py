from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',views.BLog_Main, name='blog'),
    path('blog_create',views.blog_create, name='blog_create'),
    path('blog_store',views.blog_store, name='blog_store'),
    path('blog_delete/<int:id>', views.blog_delete, name='blog_delete'),
    path('blog_edit/<int:id>', views.blog_edit, name='blog_edit'),
    path('blog_update/<int:id>', views.blog_update, name='blog_update'),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)