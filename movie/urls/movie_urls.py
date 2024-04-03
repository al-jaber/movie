from django.urls import path
from movie.views import movie_views as views


urlpatterns = [
    path('list/', views.movie_list, name='movie_list'),
    path('create/', views.create_movie, name='create_movie'),
    path('update/', views.update_movie, name='update_movie'),
    path('delete/', views.delete_movie, name='delete_movie'),
]