from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('choice_page/', views.choice_page, name='choice_page'),
    path('sign_in/', views.sign_in, name='sign_in'),
    path('sign_up/', views.sign_up, name='sign_up'),
    #path('open_sign_in', views.open_sign_in, name='open_sign_in'),
    path('open_sign_up', views.open_sign_up, name='open_sign_up'),
]