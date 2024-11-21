from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.IndexPage, name='index'),
    path('about/' , views.about, name='about'),
    path('contact/' , views.contact, name='contact'),
    path('services/' , views.services, name='services'),
    path('porojects/' , views.porojects, name='porojects'),
    ## - subscribe - ##
    path('subscribe/', views.Subscribe, name='subscribe'),
    ## - testomonialPage - ##
    path('testomonialPage/', views.testomonialPage, name='testomonialPage'),
    path('GetTestimonial/', views.GetTestimonial, name='GetTestimonial'),
    ### - admin - ### 
    path('adminIndex/', views.adminIndex, name='adminIndex'),
    path('adminy/', views.adminLogin, name='adminy'),
    path('LoginPage/', views.LoginPage, name='LoginPage'),
    ### - Project - ### 
    path('addProjectsPage/', views.addProjectsPage, name='addProjectsPage'),
    path('upProject/', views.upProject, name='upProject'),

    path('accept/', views.accept, name='accept'),
    
]
