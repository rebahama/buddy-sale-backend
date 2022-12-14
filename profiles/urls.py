from django.urls import path
from profiles import views

urlpatterns = [
     path('profiles/', views.ProfileList.as_view()),
     path('profiles/<int:pk>/', views.ProfileDetailer().as_view()),
]