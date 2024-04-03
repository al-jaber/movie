from django.urls import path
from authentication.views import user_views as views

urlpatterns = [
    path('login/', views.sign_in, name='login'),
    path('logout/', views.sign_out, name='logout'),
]