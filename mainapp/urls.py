from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/',views.about, name ='about'),
    path('services/',views.services, name ='services'),
    path('portfolio/',views.portfolio, name ='portfolio'),
    path('team/',views.team, name ='team'),
    path('contact',views.contact, name ='contact'),
    path('blog',views.blog, name ='blog'),
    path('blog-single',views.blog_single, name ='blog-single'),
    path('portfolio-details',views.portfolio, name ='portfolio-details'),
    path('contact',views.contact, name ='contact'),
]
