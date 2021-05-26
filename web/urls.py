from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cadastroC/', views.cadastro),
    path('cadastroU/', views.cadastroU),
    path('cadastroF/', views.cadastroF),
    path('cadastroP/', views.produtos),
    path('cadastroV/', views.cadastroV),
]
