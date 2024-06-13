from django.urls import path
from . import views

urlpatterns = [
    path('display', views.display, name='display'),
    path('random', views.random, name='random_notes'),
    path('postnote', views.postnote, name='postnote'),
    path('display_command/<int:note_id>', views.display_command, name='display_command'),
    path('post_command/<int:note_id>', views.post_command, name='post_command'),
]
