from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='journal-index'), 
    path('about/', views.about, name='journal-about'),
    path('<int:id>/', views.show, name='adoption-show')
]