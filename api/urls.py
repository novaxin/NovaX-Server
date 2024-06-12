
from django.urls import path
from .import views


urlpatterns = [
    path('display',views.display,name='display'),
    path('random', views.random, name='random_notes'),
    path('postnote', views.postnote, name='postnote'),
]
