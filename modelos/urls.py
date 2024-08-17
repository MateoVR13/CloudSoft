from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('modelos-servicio/', views.modelos_servicio, name='modelos_servicio'),
    path('saas/', views.saas, name='saas'),
    path('paas/', views.paas, name='paas'),
    path('iaas/', views.iaas, name='iaas'),
]
