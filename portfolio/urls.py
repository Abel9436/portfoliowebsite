from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from BLogapp import views as vw
urlpatterns = [
    path('',views.index,name='index'),
    
    path(  '',vw.blog_index, name='blog_index'),
      path('post/<int:pk>/',vw.blog_detail,name='blog_detail'),
      path('project/<int:pk>/',views.project_detail,name='project_detail'),
] + static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
