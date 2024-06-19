from django.urls import path
from . import views


urlpatterns = [
    path('display', views.display, name='display'),
    path('random', views.random, name='random_notes'),
    path('postnote', views.postnote, name='postnote'),
    path('display_user_note/<str:username>', views.display_user_note, name='display_user_note'),
    path('like_or_dislike/<str:username>', views.Like_or_Dislike, name='Like_or_Dislike'),
    
    path('display_command/<int:note_id>',views.display_command, name='display_command'),
    path('post_command/<int:note_id>', views.post_command, name='post_command'),
    
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout'),
]
