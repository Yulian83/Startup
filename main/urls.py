from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='main'),
    path('portfolio', views.portfolio, name='portfolio'),
    path('about', views.about, name='about'),
    path('response', views.response)
]