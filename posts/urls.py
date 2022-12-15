from django.urls import path
from posts import views

urlpatterns = [   
     path('posts/', views.PostList.as_view()),
     path('posts/<int:pk>/', views.PostDetalier().as_view()),
]